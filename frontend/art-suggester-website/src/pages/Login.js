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
                    {/* <!-- TODO: make this centered --> */}
                    <h3 className = "or">------------OR------------</h3>
                        <button className = "Google">Login with google</button>
                    <h3 className = "or">--------------------------</h3>
                </div>
                
            </main>    
        </>
    );
};