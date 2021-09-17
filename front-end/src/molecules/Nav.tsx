import React from "react";
import { Link } from "react-router-dom";

const Nav: React.FunctionComponent = () => {
  return (
    <nav className="navbar" role="navigation" aria-label="main navigation">
      <div className="navbar-brand">
        <Link className="navbar-item" to="google.com">
          <img
            src="https://cdn-icons-png.flaticon.com/128/1410/1410857.png"
            height="28"
          />
          <h2 className="ml-2 title is-5">Peaches</h2>
        </Link>
      </div>

      <div id="navbarBasicExample" className="navbar-menu">
        <div className="navbar-start">
          <Link className="navbar-item" to="/">
            Home
          </Link>
          <Link className="navbar-item" to="/products">
            Products
          </Link>
          <Link className="navbar-item" to="/items">
            Items
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
