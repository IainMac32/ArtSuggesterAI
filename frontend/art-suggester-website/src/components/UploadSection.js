/*
 * Harrison, Johann, Aiden
 */

import './UploadSection.css';
import DragNdrop from './DragNDrop';
import React from 'react';

export default function UploadSection({ uploadFile, setUploadFile, panelOpen, setPanelOpen }) {

    const uploadBtnClick = async () => {
        if (panelOpen || uploadFile == null) return;

        // form field and associated value
        const formData = new FormData();
        formData.append('file', uploadFile);

        try {
            // post request to the flask backend to upload the file
            const response = await fetch('http://localhost:5000/uploadFile', {
                method: 'POST',
                body: formData,
            });

            // check for upload success
            const result = await response.json();
            if (response.ok) {
                console.log('File uploaded successfully:', result);
            } else {
                console.error('Upload failed:', result);
            }
        } catch (error) {
            console.error('Error uploading file:', error);
        }

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