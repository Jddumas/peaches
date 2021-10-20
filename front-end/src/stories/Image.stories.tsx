import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import Image from "../components/Image";

export default {
  title: "components/Image",
  component: Image,
  argTypes: {
    url: {
      control: "text",
    },
  },
  decorators: [
    (Story) => (
      <div style={{ width: "300px", height: "400px" }}>
        <Story />
      </div>
    ),
  ],
} as ComponentMeta<typeof Image>;

const Template: ComponentStory<typeof Image> = (args) => (
  <Image {...args}></Image>
);
export const Primary = Template.bind({});
Primary.args = {
  url: "https://via.placeholder.com/468x60?text=HelloWorld",
};
