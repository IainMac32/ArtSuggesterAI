/*
 * Aiden Henderson & Johann Caancan
 */

import NavBar from "../components/NavBar";
import './CreateAccount.css'

export default function CreateAccount() {
    return (
        <>
            <NavBar />
            <main className="createAccount">
                <h1>Mac AI Art Suggester</h1>
                <h2>SIGN UP</h2>
                <div className = "inputs">
                    <h3 className = "inputLabel">Email</h3>
                    <input className = "loginInput" placeholder="user@domain.com"></input>
                    <h3 className = "inputLabel">Password</h3>
                    <input className = "loginInput" placeholder="password123"></input>
                    <h3 className = "inputLabel">Verify Password</h3>
                    <input className = "loginInput" placeholder="password123"></input>
                    <button className = "Login">Create Account</button>
                    <div className = 'halfLine'></div> 
                    <h3 className = "or">OR</h3>
                    <div className = 'halfLine'></div>
                    <button className = "Google"><img src="/images/GoogleLogo.png" alt="logo" className='google-logo' />Sign up with google</button>
                    <div className = 'line'></div>
                    <p className="noAcc">Already have an account? <a href = '/login'>Log in!</a></p>
                </div>
                
            </main>    
        </>
    );
};