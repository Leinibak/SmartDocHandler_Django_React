import React from "react";
import "../styles/Pattern.css"

function Pattern({ pattern, handleDelete }) {
    return (
        <div key={pattern.id} className="pattern-container">
            <h3 className="pattern-title">Title : {pattern.title}</h3>
            <p className="pattern-content">Customer : {pattern.customer}</p>
            <p className="pattern-content">Pattern : {pattern.pattern}</p>
            <p className="pattern-date"> Created at : 
                {new Date(pattern.created_at).toLocaleString()} 
            </p>
            <button
                className="delete-button"
                onClick={() => handleDelete(pattern.id)}
            >
                Delete
            </button>
        </div>
    );
}

export default Pattern
