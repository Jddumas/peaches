import React from "react";
import Nav from "./molecules/Nav";
import HomeHero from "./molecules/HomeHero";
import Router from "./Router";
import { BrowserRouter } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <Nav></Nav>
        <Router />
      </div>
    </BrowserRouter>
  );
}

export default App;
