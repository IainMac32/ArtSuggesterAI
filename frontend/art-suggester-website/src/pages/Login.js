import NavBar from "../components/NavBar";
import './Login.css';

export default function Login() {
    return (
        <>
            <NavBar />
            <main className="loginPage">
                <h1>Mac AI Art Suggester</h1>
                <h2>LOG IN</h2>
                <div className = "inputs">
                    <h3 className = "inputLabel">Email</h3>
                    <input className = "loginInput" placeholder="johndoe@gmail.com"></input>
                    <h3 className = "inputLabel">Password</h3>
                    <input className = "loginInput" placeholder="password123"></input>
                    <div className = 'halfLine'></div> 
                    <h3 className = "or">OR</h3>
                    <div className = 'halfLine'></div>
                    <button className = "Google"><img src="/images/GoogleLogo.png" alt="logo" className='google-logo' />Login with google</button>
                    <div className = 'line'></div>
                    <p className="noAcc">Don't have an account? <a href = '/createAccount'>Register now</a></p>

                </div>
                
            </main>    
        </>
    );
};