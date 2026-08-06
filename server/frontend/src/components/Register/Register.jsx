import React, { useState } from 'react';
import "./Register.css";
import "../assets/style.css";
import Header from '../Header/Header';

const Register = ({ onClose }) => {
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");

    let register_url = window.location.origin+"/djangoapp/register";

    const register = async (e) => {
        e.preventDefault();
        const res = await fetch(register_url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "userName": userName,
                "password": password,
                "firstName": firstName,
                "lastName": lastName,
                "email": email
            }),
        });

        const json = await res.json();
        if (json.status != null && json.status === "Authenticated") {
            sessionStorage.setItem('username', json.userName);
            sessionStorage.setItem('firstname', firstName);
            sessionStorage.setItem('lastname', lastName);
            window.location.href = "/";
        }
        else {
            alert("The user could not be registered.");
        }
    };

    return (
        <div>
            <Header/>
            <form className="register_container" onSubmit={register}>
                <h1 className="header" style={{textAlign:"center"}}>Register</h1>
                <div className="inputs">
                    <div className="input">
                        <input type="text" name="username" placeholder="Username" className="input_field" onChange={(e) => setUserName(e.target.value)} required/>
                    </div>
                    <div className="input">
                        <input type="text" name="firstname" placeholder="First Name" className="input_field" onChange={(e) => setFirstName(e.target.value)} required/>
                    </div>
                    <div className="input">
                        <input type="text" name="lastname" placeholder="Last Name" className="input_field" onChange={(e) => setLastName(e.target.value)} required/>
                    </div>
                    <div className="input">
                        <input type="email" name="email" placeholder="Email" className="input_field" onChange={(e) => setEmail(e.target.value)} required/>
                    </div>
                    <div className="input">
                        <input type="password" name="password" placeholder="Password" className="input_field" onChange={(e) => setPassword(e.target.value)} required/>
                    </div>
                    <div className="submit_panel">
                        <button className="submit" type="submit">Register</button>
                    </div>
                </div>
            </form>
        </div>
    );
};

export default Register;
