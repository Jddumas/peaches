import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import ProductTable from "../components/ProductTable";
import { mockProducts } from "../mocks/mock_data";

export default {
  title: "components/ProductTable",
  component: ProductTable,
  args: {
    products: mockProducts,
    headers: Object.keys(mockProducts[0]),
    cellFormatter: (data, header) => {
      if (header === "thumbnail_url") {
        return <img src={data} alt="image" className="image is-48x48" />;
      } else return <span>{data}</span>;
    },
  },
} as ComponentMeta<typeof ProductTable>;

const Template: ComponentStory<typeof ProductTable> = (args) => (
  <ProductTable {...args}></ProductTable>
);

export const Primary = Template.bind({});
