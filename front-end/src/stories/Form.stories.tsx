import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import Form from "../components/Form";
import { mockProducts } from "../mocks/mock_data";

export default {
  title: "components/Form",
  component: Form,
  argTypes: {
    onSubmit: {
      action: "submitted",
    },
    fieldConfigs: {
      defaultValue: [
        {
          label: "name",
          inputType: "text",
          required: true,
          placeHolder: "Name of the product",
          key: "name",
          constraints: {
            required: true,
          },
        },
        {
          label: "description",
          inputType: "multiline-text",
          required: true,
          key: "description",
        },
        {
          label: "brand",
          inputType: "text",
          key: "brand",
          constraints: {
            required: true,
          },
        },
        {
          label: "category",
          inputType: "text",
          key: "category",
          constraints: {
            required: true,
          },
        },
        {
          label: "price",
          inputType: "number",
          key: "price",
          constraints: {
            required: true,
            min: 0,
          },
        },
        {
          label: "weight",
          inputType: "number",
          key: "weight",
          constraints: {
            required: true,
          },
        },
        {
          label: "stock",
          inputType: "number",
          key: "stock",
          constraints: {
            required: true,
            min: 12,
          },
        },
        {
          label: "thumbnail image",
          inputType: "text",
          key: "thumbnail_url",
        },
        {
          label: "shelf life",
          inputType: "number",
          key: "shelf_life",
          constraints: {
            required: true,
            min: 0,
          },
        },
      ],
    },
  },
} as ComponentMeta<typeof Form>;

const Template: ComponentStory<typeof Form> = (args) => <Form {...args}></Form>;
export const Creation = Template.bind({});
export const Modification = Template.bind({});
Modification.args = {
  defaultValue: mockProducts[0],
};
