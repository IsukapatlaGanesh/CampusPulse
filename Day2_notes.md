# Day 2 Notes

## Folder Structure

CampusPulse/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css


## Purpose of Each Folder

templates/
- stores HTML pages

static/
- stores CSS, JavaScript, images

css/
- stores stylesheet files

app.py
- main backend Flask file


## New Flask Concepts

from flask import Flask, render_template
- render_template allows Flask to send HTML pages

render_template('index.html')
- renders HTML page from templates folder

{{ url_for('static', filename='css/style.css') }}
- connects CSS file properly in Flask


## HTML Learned

<link rel="stylesheet">
- links CSS file

<h1>
- heading

<p>
- paragraph


## CSS Learned

body
- styles entire webpage

background-color
- changes background

color
- changes text color

font-family
- changes font

text-align
- aligns text

margin-top
- creates top spacing


## Commands Used

python app.py
- runs Flask server

git add .
- stages changes

git commit -m "message"
- creates checkpoint

git push
- uploads code to GitHub


## Important Understanding

Backend:
- Flask handles server and routes

Frontend:
- HTML creates structure
- CSS styles webpage

Flask connects backend and frontend together.


## Day 2 Result

- Flask now renders real webpage
- CSS connected successfully
- Proper project structure created