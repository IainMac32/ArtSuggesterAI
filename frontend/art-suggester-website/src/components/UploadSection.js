/*
 * Harrison Johns
 *  Contact before making changes
 */

import './UploadSection.css';

export default function UploadSection() {
    return (
        <>
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