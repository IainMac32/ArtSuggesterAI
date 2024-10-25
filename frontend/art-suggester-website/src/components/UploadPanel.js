/*
 * Harrison Johns
 */

import React, { useState } from "react"
import './UploadPanel.css'

const UploadPanel = (uploadFile) => {
  // States to hold the detected color information
  // this states should be retrieved from backend
  const [detectedColors, setDetectedColors] = useState('{red, blue, yellow, ...}');
  const [detectedMaterials, setDetectedMaterials] = useState('{pencil crayons, paint, marker, ...}');

  const handleConfirm = () => {
    console.log("Confirmed!");
  };

  return (
    <div className="upload-details-panel">
      <h2 className="panel-title">Upload Details</h2>
      
      <div className="upload-details-columns">
        <div>
            <div className="input-group">
            <label>Colours Detected</label>
            <textarea
              value={detectedColors}
              readOnly
              className="detected-info"
            />
          </div>

          <div className="input-group">
            <label>Colours Detected</label>
            <textarea
              value={detectedMaterials}
              readOnly
              className="detected-info"
            />
          </div>

          <button
            onClick={handleConfirm}
            className="confirm-button"
          >
            Confirm
          </button>
        </div>
        <div className="image-placeholder">
        <svg
          className="image-icon"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M3 7l8-4 8 4m-8 6v10M3 17l8-4 8 4"
          ></path>
        </svg>
      </div>
      </div>
    </div>
  );
}

export default UploadPanel