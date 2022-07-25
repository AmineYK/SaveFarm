import React, { useState } from "react";


import "../components/imagepicker.scss"
import CardPredicted from "./cardpredicted";

const ImagePicker = ({ setImage }) => {
  const [classOnDrag, setClassOnDrag] = useState("");
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [predicted , setPredicted] = useState(null)
  const [confidence , setConfidence] = useState(null)

  const axios = require("axios").default;
  

  const sendFile = async (file) => {
	  console.log("IS SENDING")
      let formData = new FormData();
      formData.append("file", file);
      let res = await axios({
        method: "post",
        url:"http://localhost:8000/predict",
        data: formData,
      });
      if (res.status === 200) {
		setPredicted(res.data.class)
		setConfidence(res.data.confidence)
      }
  }

  const upload = (files) => {
    if (files.length !== 1) return;

    // setImage(files[0]);
    setFile(files[0]);
    setPreview(URL.createObjectURL(files[0]));
	sendFile(files[0])
  };

  return (
	<div className="IP">
    <section className="imagepicker">
      <div className={`imagepicker-dropzone ${classOnDrag}`}>
        {file ? (
          <span className="predicted">{predicted}</span>
        ) : (
          "Drag and drop image here, or click to select image"
        )}
        <input
          type="file"
          name="image"
          accept="image/png, image/jpeg"
          onChange={(e) => upload(e.target.files)}
          onDragEnter={() => setClassOnDrag("drag")}
          onDragLeave={() => setClassOnDrag("")}
        />
      </div>

      {file && (
        <img
          src={preview}
          alt="selected-image"
          className="imagepicker-image"
          onLoad={() => URL.revokeObjectURL(preview)}
        />
      )}




    </section>
			{
				predicted !== null &&
				<CardPredicted type={predicted} confidence={confidence} file={file} />
			}
	</div>
  );
};

export default ImagePicker;
