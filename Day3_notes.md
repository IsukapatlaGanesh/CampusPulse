# Day 3 Notes

## Goal of Day 3

Create a complaint submission form and connect frontend with Flask backend.


## New HTML Concepts

<form>
- collects user input

action="/submit"
- sends form data to Flask submit route

method="POST"
- sends data securely to backend

<input>
- single line user input

<textarea>
- multi-line input field

<button>
- submits form


## Important Attribute

name="title"
name="description"

- backend uses these names to identify form data


## New Flask Concepts

from flask import request

- request object handles incoming form data


@app.route('/submit', methods=['POST'])

- creates route for handling submitted form data
- methods=['POST'] allows POST requests


## Accessing Form Data

request.form['title']
request.form['description']

- retrieves values entered by user


## Full Data Flow

User enters data
→ Form submits data
→ POST request sent
→ Flask receives data
→ Backend processes it
→ Response displayed


## CSS Learned

input, textarea
- styling form fields

button
- styling submit button

padding
- spacing inside element

border-radius
- rounded corners

cursor: pointer
- hand cursor on hover


## Important Understanding

Frontend and backend are now connected successfully.

HTML form sends data to Flask backend using POST request.


## Commands Used

python app.py
- runs Flask server

git add .
- stages files

git commit -m "message"
- creates checkpoint

git push
- uploads changes to GitHub


## Day 3 Result

- Complaint submission form created
- Flask receives form data
- User input displayed successfully
- Frontend ↔ Backend communication working