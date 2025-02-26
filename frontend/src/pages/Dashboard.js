import React from "react";
import { Button, Container, Typography } from "@mui/material";
import { Link } from "react-router-dom";

const Dashboard = () => {
  return (
    <Container>
      <Typography variant="h3">Admin Dashboard</Typography>
      <Button component={Link} to="/events" variant="contained" color="primary">Manage Events</Button>
      <Button component={Link} to="/volunteers" variant="contained" color="secondary">Manage Volunteers</Button>
      <Button component={Link} to="/hours-tracking" variant="contained" color="success">Track Volunteer Hours</Button>
    </Container>
  );
};

export default Dashboard;
