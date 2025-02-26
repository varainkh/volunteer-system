import React, { useState, useEffect } from "react";
import axios from "axios";
import { Button, TextField, Container, List, ListItem, ListItemText } from "@mui/material";

const Events = () => {
  const [events, setEvents] = useState([]);
  const [newEvent, setNewEvent] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/events/").then((res) => setEvents(res.data));
  }, []);

  const addEvent = async () => {
    await axios.post("http://127.0.0.1:8000/api/events/", { name: newEvent });
    setNewEvent("");
    window.location.reload();
  };

  return (
    <Container>
      <TextField fullWidth label="New Event" value={newEvent} onChange={(e) => setNewEvent(e.target.value)} />
      <Button onClick={addEvent} variant="contained" color="primary">Add Event</Button>
      <List>
        {events.map((event) => (
          <ListItem key={event.id}>
            <ListItemText primary={event.name} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default Events;
