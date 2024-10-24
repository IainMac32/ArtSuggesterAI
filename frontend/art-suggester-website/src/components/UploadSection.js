/*
 * Harrison Johns
 *  Contact before making changes
 */

import './UploadSection.css';
import DragNdrop from './DragNDrop';
import React from 'react';
import { useState } from 'react';

export default function UploadSection() {
    
    const [files, setFiles] = useState([]);

    return (
        <>
            <DragNdrop onFilesSelected={setFiles} width="300px" height='400px'/>
            <div className="upload-section">
                <label htmlFor="file-upload" className="upload-label">
                    Upload image(s) here:
                </label>
                <div className="upload-box">
                    <input type="file" id="file-upload" className="file-input" />
                    <i className="upload-icon">📁</i>
                </div>
                <button className="upload-btn">Upload</button>
                <p>Supported file types: .pdf, .jpg, .webp, ...</p>
            </div>
        </>
    );
};