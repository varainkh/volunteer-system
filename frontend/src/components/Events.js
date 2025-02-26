import React, { useEffect, useState } from "react";
import axios from "axios";
import { API_BASE_URL } from "../config";

function Events() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get(`${API_BASE_URL}/events/`)
            .then(response => setEvents(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Events List</h2>
            <ul>
                {events.map(e => (
                    <li key={e.id}>{e.title} - {e.date}</li>
                ))}
            </ul>
        </div>
    );
}

export default Events;
