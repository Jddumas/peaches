import React, { ReactElement, ReactNode } from "react";
import { useForm } from "react-hook-form";

type ValidatorFn = (value: string | number) => boolean;
type FormProps<T> = {
  defaultValue?: T;
  fieldConfigs: FieldConfig<keyof T>[];
  onSubmit: VoidFunction;
};
type FieldConfig<IK> = {
  label: string;
  inputType: "text" | "number" | "multiline-text";
  placeHolder?: string;
  key: IK;
  constraints?: FieldConstraints;
  helpTexts?: HelpTexts;
};
type FieldConstraints = {
  required?: boolean;
  min?: number;
  max?: number;
  maxLength?: number;
  minLength?: number;
  pattern?: RegExp;
  validate?: ValidatorFn | { [key: string]: ValidatorFn };
};
type FieldConstraintsKey = keyof FieldConstraints;
type HelpTexts = { [k in FieldConstraintsKey]: string | Element };

function makeDefaultHelpText<T>(fieldConfigs: FieldConfig<T>) {
  const { key, helpTexts, constraints = {} } = fieldConfigs;
  const existingHelpTexts = Object.keys(helpTexts || {});

  const fKey = ((key as unknown) as string)
    .toString()
    .replace(/^\w/, (c) => c.toUpperCase());

  let generatedTexts: Partial<HelpTexts> = {};

  if (!existingHelpTexts.includes("required")) {
    generatedTexts.required = `${fKey} is missing.`;
  }
  if (!existingHelpTexts.includes("min") && !!constraints["min"]) {
    generatedTexts.min = `${fKey} needs to be larger than ${constraints["min"]}.`;
  }
  if (!existingHelpTexts.includes("max") && !!constraints["max"]) {
    generatedTexts.maxLength = `${fKey} needs to be smaller than ${constraints["max"]}.`;
  }
  if (!existingHelpTexts.includes("maxLength") && !!constraints["maxLength"]) {
    generatedTexts.maxLength = `${fKey} needs to be at most ${constraints["maxLength"]} characters.`;
  }
  if (!existingHelpTexts.includes("minLength") && !!constraints["minLength"]) {
    generatedTexts.minLength = `${fKey} needs to be at least ${constraints["minLength"]} characters.`;
  }
  if (!existingHelpTexts.includes("pattern") && !!constraints["pattern"]) {
    generatedTexts.pattern = `${fKey} needs to match pattern ${constraints.pattern}.`;
  }

  return { ...fieldConfigs, helpTexts: { ...helpTexts, ...generatedTexts } };
}

function Form<T>(props: FormProps<T>): ReactElement {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({ defaultValues: props.defaultValue, mode: "onBlur" });

  const enrichedFieldConfigs = props.fieldConfigs.map((f) =>
    makeDefaultHelpText(f)
  );

  return (
    <div>
      <form className="form" onSubmit={handleSubmit(props.onSubmit)}>
        {enrichedFieldConfigs.map((fieldConfig) => {
          return (
            <div className="field" key={fieldConfig.key.toString()}>
              <label className="label">
                <span className="is-capitalized">{fieldConfig.label}</span>{" "}
                {fieldConfig.constraints?.required && (
                  <strong className="has-text-danger">*</strong>
                )}
              </label>
              <div className="control">
                {fieldConfig.inputType != "multiline-text" ? (
                  <input
                    {...register(
                      fieldConfig.key.toString(),
                      fieldConfig.constraints
                    )}
                    className="input"
                    type={fieldConfig.inputType}
                    placeholder={fieldConfig.placeHolder}
                    step="0.01"
                  />
                ) : (
                  <textarea
                    className="textarea "
                    placeholder={fieldConfig.placeHolder}
                    {...register(
                      fieldConfig.key.toString(),
                      fieldConfig.constraints
                    )}
                  ></textarea>
                )}
              </div>
              {errors[fieldConfig.key.toString()] && fieldConfig.helpTexts && (
                <p className="help is-danger has-text-weight-medium">
                  {
                    fieldConfig.helpTexts[
                      errors[fieldConfig.key.toString()]
                        .type as FieldConstraintsKey
                    ]
                  }
                </p>
              )}
            </div>
          );
        })}
        <div className="field is-grouped">
          <div className="control">
            <button className="button is-link">Submit</button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default Form;
