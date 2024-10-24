/*
 * Harrison Johns
 *  Contact before making changes
 * 
 * To-be-added:
 * get profile pic from firebase
 */

import './NavBar.css';

export default function NavBar() {
    return (
        <header className='nav-header'>
            <nav className='nav'>
                <img src="/logo.png" alt="logo" className='nav-logo' />
                <ul className='nav-links'>
                    <li><a href="/">Home</a></li>
                    <li><a href="/favourites">Favourites</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
                <div className='user-section'>
                    <img src="/profile-pic.png" alt="profile" className='nav-profile-pic' />
                    <a href="/login">Log In / Register</a>
                </div>
            </nav>
        </header>
    )
}