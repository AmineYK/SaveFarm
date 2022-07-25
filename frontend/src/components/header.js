import React from 'react'
import "../components/header.css"
import logo from '../../src/Images/cblogo.PNG'

export default function header() {
  return (
	<div className='header'>
		<p>Protect your products & boost their quality with <span>SaveFarm</span> </p>
		<img src={logo}></img>
	</div>
  )
}
