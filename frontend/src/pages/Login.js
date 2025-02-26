import React, { useState, useContext } from "react";
import axios from "axios";
import { Button, TextField, Container, Typography } from "@mui/material";
import AuthContext from "../context/AuthContext";

const Login = () => {
  const { login } = useContext(AuthContext);
  const [credentials, setCredentials] = useState({ username: "", password: "" });
  const [error, setError] = useState("");

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/accounts/login/", credentials);
      login(response.data.token);
      window.location.href = "/dashboard";
    } catch (err) {
      setError("Invalid Credentials");
    }
  };

  return (
    <Container maxWidth="xs">
      <Typography variant="h4" gutterBottom>Login</Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField fullWidth label="Username" onChange={(e) => setCredentials({ ...credentials, username: e.target.value })} margin="normal" />
      <TextField fullWidth label="Password" type="password" onChange={(e) => setCredentials({ ...credentials, password: e.target.value })} margin="normal" />
      <Button variant="contained" color="primary" onClick={handleLogin} fullWidth>Login</Button>
    </Container>
  );
};

export default Login;
