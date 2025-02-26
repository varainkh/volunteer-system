import React, { useEffect, useState } from "react";
import axios from "axios";
import { API_BASE_URL } from "../config";

function Volunteers() {
    const [volunteers, setVolunteers] = useState([]);

    useEffect(() => {
        axios.get(`${API_BASE_URL}/volunteers/`)
            .then(response => setVolunteers(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Volunteers List</h2>
            <ul>
                {volunteers.map(v => (
                    <li key={v.id}>{v.name} - {v.email}</li>
                ))}
            </ul>
        </div>
    );
}

export default Volunteers;
