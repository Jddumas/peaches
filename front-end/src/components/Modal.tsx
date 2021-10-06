import React, { ReactNode } from "react";

type ModalProps = {
  open: boolean;
  onRequestClose: VoidFunction;
  children: ReactNode;
  footer: ReactNode;
  title: string;
};

const Modal: React.VFC<ModalProps> = ({
  open,
  onRequestClose,
  children,
  title,
  footer,
}) => {
  return (
    <div className={`modal ${open ? "is-active" : ""}`}>
      <div className="modal-background"></div>
      <div className="modal-card">
        <header className="modal-card-head has-background-white">
          <p className="modal-card-title">{title}</p>
          <button
            className="delete"
            aria-label="close"
            onClick={onRequestClose}
          ></button>
        </header>
        <section className="modal-card-body">{children}</section>
        {footer ? <footer className="modal-card-foot">{footer}</footer> : null}
      </div>
    </div>
  );
};

export default Modal;
