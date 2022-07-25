import React from 'react'
import Header from './header'
import '../components/home.css'
import ImagePicker from "../components/imagepicker.js"

export default function home() {
  return (
	<div className='home'>
		<Header />
		<ImagePicker />
	</div>
  )
}
