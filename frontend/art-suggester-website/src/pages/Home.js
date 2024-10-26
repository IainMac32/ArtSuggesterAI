/*
 * Harrison Johns
 */

import React from "react";
import { useState } from "react";
import NavBar from "../components/NavBar";
import UploadSection from "../components/UploadSection";
import './Home.css';
import UploadPanel from "../components/UploadPanel";

export default function Home() {

    const [uploadFile, setUploadFile] = useState(null);
    const [uploadPanelOpen, setUploadPanelOpen] = useState(false);

    return (
        <>
            <NavBar />
            { uploadPanelOpen && ( <>
                <div className="overlay">
                    <UploadPanel img_url={URL.createObjectURL(uploadFile)} closePanel={() => setUploadPanelOpen(false)} />
                </div>
            </>)}

            <main className="main-section">
                <h1>Art Suggester AI</h1>
                <p className="home-subtitle">- from the <a href="/about">McMaster AI Society</a></p>
                <UploadSection 
                    uploadFile={uploadFile} 
                    setUploadFile={setUploadFile} 
                    panelOpen={uploadPanelOpen}
                    setPanelOpen={setUploadPanelOpen}
                />
            </main>
        </>
    );
};