import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";
import Modal from "../components/Modal";
import { mockProducts } from "../mocks/mock_data";

export default {
  title: "components/Modal",
  component: Modal,
  argTypes: {
    open: {
      control: "boolean",
      defaultValue: false,
    },
    children: {
      defaultValue: <p>Ipsum Lorem...</p>,
    },
    onRequestClose: {
      defaultValue: () => {},
    },
    title: {
      control: "text",
      defaultValue: "Hello, world",
    },
  },
} as ComponentMeta<typeof Modal>;

const Template: ComponentStory<typeof Modal> = (args) => (
  <Modal {...args}></Modal>
);
export const Primary = Template.bind({});
