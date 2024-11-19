import React, { useState, useEffect, Component } from "react";
import api from "../api";
import "../styles/Home.css";
import "../styles/Pattern.css";
import Pattern from "../components/Pattern"

function Home() {
    const [patterns, setPatterns] = useState([]);
    const [form, setForm] = useState({
        customer: "",
        title: "",
        category: "invoice", // 기본값
        region: "domestic",  // 기본값
        pattern: "",
    });

    const fetchPatterns = async () => {
        try {
            const response = await api.get("/api/patterns/");
            setPatterns(response.data);
           // console.log(response.data);
        } catch (error) {
            console.error("Error fetching patterns:", error);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm({ ...form, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post("/api/patterns/", form);
            setPatterns([...patterns, response.data]); // 새로운 패턴 추가
            setForm({
                customer: "",
                title: "",
                category: "invoice", // 기본값
                region: "domestic",  // 기본값
                pattern: "",
            });
        } catch (error) {
            console.error("Error creating pattern:", error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await api.delete(`/api/patterns/${id}/`);
            setPatterns(patterns.filter((pattern) => pattern.id !== id));
        } catch (error) {
            console.error("Error deleting pattern:", error);
        }
    };

    useEffect(() => {
        fetchPatterns();
    }, []);

    return (
        
        <div> 
            <div className="form-create-pattern-container">
                {/* 패턴 생성 폼 */}

                <h1>Pattern Management</h1>
                <form onSubmit={handleSubmit}>
                    <div >
                        <h2>Create new Pattern</h2>
                        <label>Customer:</label>
                        <input
                            type="text"
                            name="customer"
                            value={form.customer}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label>Title:</label>
                        <input  
                            type="text"
                            name="title"
                            value={form.title}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label>Category:</label>
                        <select
                            name="category"
                            value={form.category}
                            onChange={handleChange}
                            required
                        >
                            <option value="invoice">Invoice</option>
                            <option value="credit">Credit</option>
                        </select>
                    </div>
                    
                    <div>
                        <label>Region:</label>
                        <select
                            name="region"
                            value={form.region}
                            onChange={handleChange}
                            required
                        >
                            <option value="domestic">Domestic</option>
                            <option value="foreign">Foreign</option>
                        </select>
                    </div>
                    <div>
                        <label>Pattern:</label>
                        <textarea
                            name="pattern"
                            value={form.pattern}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit">Create Pattern</button>
                </form>
            </div>
            <div  className="pattern-container">
                <h2>Existing Patterns</h2>
                {patterns.map((pattern) => (<Pattern pattern={pattern} handleDelete={handleDelete} key={pattern.id} /> ))}
            </div>
        </div>
    );
}


export default Home;
