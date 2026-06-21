# Day 8 Notes – Routing Mastery

## What is a Route?

A route maps a URL to a Python function.

Example:

@app.route('/complaints')

means:

If user visits /complaints,
run complaints().


## GET Request

Used to retrieve pages/data.

Examples:

GET /
GET /complaints


## POST Request

Used to send data.

Example:

POST /submit


## CampusPulse Route Map

/              → Homepage

/submit        → Save complaint

/complaints    → Display complaints


## Application Flow

Homepage:
Browser → GET / → home() → index.html

Submit:
Browser → POST /submit → submit() → Database

View Complaints:
Browser → GET /complaints → complaints() → complaints.html


## Important Understanding

Routes are the addresses of a web application.

Flask uses routes to decide which function should run.


## Day 8 Result

- Understood routing.
- Learned GET vs POST.
- Created route map.
- Connected HTML links/forms with Flask functions.