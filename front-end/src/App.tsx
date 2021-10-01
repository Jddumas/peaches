import React from "react";
import Nav from "./molecules/Nav";
import Router from "./Router";
import { BrowserRouter } from "react-router-dom";
import { RecoilRoot } from "recoil";

function App() {
  return (
    <BrowserRouter>
      <RecoilRoot>
        <div className="container">
          <Nav></Nav>
          <Router />
        </div>
      </RecoilRoot>
    </BrowserRouter>
  );
}

export default App;
