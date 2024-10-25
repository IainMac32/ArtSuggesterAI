/*
 * Harrison Johns
 */

import './UploadSection.css';
import DragNdrop from './DragNDrop';
import React from 'react';
import { useState } from 'react';

export default function UploadSection({ uploadFile, setUploadFile }) {
    
    return (
        <>
            <div className="upload-section">
                <DragNdrop uploadFile={uploadFile} setUploadFile={setUploadFile}/>
                <button className="upload-btn">Upload</button>
                <p>Supported file types: .pdf, .jpg, .webp, ...</p>
            </div>
        </>
    );
};