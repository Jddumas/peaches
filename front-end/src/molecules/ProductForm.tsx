import React, { useState } from "react";
import Form, { FieldConfig } from "../components/Form";
import Image from "../components/Image";
import { Product } from "../entity";

type ProductFormProps = {
  product?: Product;
};
const productFormConfigs: FieldConfig<keyof Product>[] = [
  {
    label: "name",
    inputType: "text",
    placeHolder: "Name of the product",
    key: "name",
    constraints: {
      required: true,
    },
  },
  {
    label: "description",
    inputType: "multiline-text",
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
];
const ProductForm: React.VFC<ProductFormProps> = ({ product }) => {
  const [imgSrc, setImgSrc] = useState(product?.thumbnail_url);
  return (
    <div className="box">
      <p className="title">Update or Change Product</p>
      <div className="columns">
        <div className="column">
          <Image url={imgSrc!} className="left"></Image>
        </div>
        <div className="column">
          <Form
            defaultValue={product}
            fieldConfigs={productFormConfigs}
            onSubmit={() => alert("You won")}
            onFieldsBlur={(value, name) => {
              if (name === "thumbnail_url") {
                setImgSrc(value.thumbnail_url);
              }
            }}
          ></Form>
        </div>
      </div>
    </div>
  );
};

export default ProductForm;
