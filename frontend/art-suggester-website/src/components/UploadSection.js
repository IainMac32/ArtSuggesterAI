/*
 * Harrison Johns
 */

import './UploadSection.css';
import DragNdrop from './DragNDrop';
import React from 'react';

export default function UploadSection({ uploadFile, setUploadFile, panelOpen, setPanelOpen }) {

    const uploadBtnClick = () => {
        if (panelOpen || uploadFile == null) return;

        setPanelOpen(true);
    }

    return (
        <>
            <div className="upload-section">
                <DragNdrop uploadFile={uploadFile} setUploadFile={setUploadFile}/>
                <button className="upload-btn" onClick={uploadBtnClick}>Upload</button>
                <p>Supported file types: .pdf, .jpg, .webp, ...</p>
            </div>
        </>
    );
};