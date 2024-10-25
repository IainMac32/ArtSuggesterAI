/*
 * Harrison Johns
 */

import React from "react";
import { useState } from "react";
import NavBar from "../components/NavBar";
import UploadSection from "../components/UploadSection";
import Blur from "../components/Blur";
import './Home.css';

export default function Home() {

    const [filesUploaded, setFilesUploaded] = useState(false);

    return (
        <>
            <NavBar />
            <Blur />

            <main className="main-section">
                <h1>Art Suggester AI</h1>
                <p className="home-subtitle">- from the <a href="/about">McMaster AI Society</a></p>
                <UploadSection />
            </main>
        </>
    );
};