import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import ProductForm from "../molecules/ProductForm";
import { mockProducts } from "../mocks/mock_data";

export default {
  title: "components/ProductForm",
  component: ProductForm,
} as ComponentMeta<typeof ProductForm>;

const Template: ComponentStory<typeof ProductForm> = (args) => (
  <ProductForm {...args}></ProductForm>
);
export const Creation = Template.bind({});
export const Modification = Template.bind({});
Modification.args = {
  product: mockProducts[0],
};
