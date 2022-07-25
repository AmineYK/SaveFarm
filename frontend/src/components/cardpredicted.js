
import React, { Component, useState } from 'react'
import "../components/cardpredicted.css"


const axios = require("axios").default;






const CardPredicted  = ({file,type})  =>{
	
	const [predicted , setPredicted] = useState(null)
	
	const sendFile = async (file,type) => {
		let formData = new FormData();
		formData.append("file", file);
		let res = await axios({
		  method: "post",
		  url:"http://localhost:8000/predict"+type,
		  data: formData,
		});
		if (res.status === 200) {
			setPredicted(res.data.class)
		}
	}
	return(


		<div className='cardP' onClick={() => sendFile(file,type)}>
			<span><p>Verify Health</p></span>
			{predicted !== null && <p>{predicted}</p>}
		
		</div>

	)

}

export default CardPredicted

