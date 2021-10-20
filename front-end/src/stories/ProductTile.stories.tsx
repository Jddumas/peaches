import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import ProductTile from "../components/ProductTile";
import { mockProducts } from "../mocks/mock_data";

export default {
  title: "components/ProductTile",
  component: ProductTile,
} as ComponentMeta<typeof ProductTile>;

// const Template: ComponentStory<typeof ProductTile> = (args) => (
//   <ProductTile {...args} />
// );

export const Primary = () => <ProductTile product={mockProducts[0]} />;
