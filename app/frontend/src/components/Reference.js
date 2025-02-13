import React from 'react'
import { useDispatch } from 'react-redux'
import { updateRef } from '../store/references/actions'

export const Reference = ({ reference, showNewReferenceForm }) => {
	const dispatch = useDispatch()

	return (
		<>
			<div className='w3-row'>
				<div className='w3-quarter'>
					<p><b>First author</b></p>
				</div>
				<div className='w3-rest'>
					<p><b>{reference.firstAuthor}</b></p>
				</div>
			</div>
			<div className='w3-row'>
				<div className='w3-quarter'>
					<p><b>Year</b></p>
				</div>
				<div className='w3-rest'>
					<p><b>{reference.year}</b></p>
				</div>
			</div>
			<div className='w3-row'>
				<div className='w3-quarter'>
					<p><b>Title</b></p>
				</div>
				<div className='w3-rest'>
					<p><b>{reference.title}</b></p>
				</div>
			</div>
			<div className='w3-row'>
				<div className='w3-quarter'>
					<p><b>DOI</b></p>
				</div>
				<div className='w3-rest'>
					<p><b>{reference.doi}</b></p>
				</div>
			</div>
			<div className='w3-row'>
				<div className='w3-quarter'>
					<p><b>Link</b></p>
				</div>
				<div className='w3-rest'>
					<p><b>{reference.link}</b></p>
				</div>
			</div>
			<button
				className='w3-button w3-grey'
				onClick={() => {
					dispatch(updateRef({ ...reference, edit: true }))
					showNewReferenceForm()
				}}
			>
				Edit
			</button>
		</>
	)
}
