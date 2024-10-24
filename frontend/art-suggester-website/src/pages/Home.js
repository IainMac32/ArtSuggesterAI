/*
 * Harrison Johns
 *  Contact before making changes
 */

import NavBar from "../components/NavBar";
import UploadSection from "../components/UploadSection";
import './Home.css';

export default function Home() {
    return (
        <>
            <NavBar />
            <main className="main-section">
                <h1>Art Suggester AI</h1>
                <p>- from the McMaster AI Society</p>
                <UploadSection />
            </main>
        </>
    );
};