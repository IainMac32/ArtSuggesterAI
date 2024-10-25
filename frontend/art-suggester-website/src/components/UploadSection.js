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
            <div className="upload-section">
                <DragNdrop onFilesSelected={setFiles}/>
                <button className="upload-btn">Upload</button>
                <p>Supported file types: .pdf, .jpg, .webp, ...</p>
            </div>
        </>
    );
};