import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav style={{ padding: "10px", background: "#007bff", color: "#fff" }}>
            <Link to="/" style={{ margin: "10px", color: "#fff" }}>Dashboard</Link>
            <Link to="/volunteers" style={{ margin: "10px", color: "#fff" }}>Volunteers</Link>
            <Link to="/events" style={{ margin: "10px", color: "#fff" }}>Events</Link>
            <Link to="/login" style={{ margin: "10px", color: "#fff" }}>Login</Link>
            <Link to="/register" style={{ margin: "10px", color: "#fff" }}>Register</Link>
        </nav>
    );
}

export default Navbar;
