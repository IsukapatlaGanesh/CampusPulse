# Day 6 Notes

## Goal of Day 6

Upgrade complaints from simple text entries to structured issue records.

Before:

Complaint
├── Title
└── Description

After:

Complaint
├── Title
├── Description
├── Category
└── Status


## New Features Added

- Category dropdown
- Automatic status assignment
- Category badge display
- Status badge display


## New HTML Concept

<select>

- Creates dropdown menu
- Restricts user to predefined options

Example categories:
- Infrastructure
- Technology
- Hygiene
- Academic


## New Backend Concepts

category = request.form['category']

- Receives selected category from form

status = "Pending"

- Automatically assigns default status


## New Database Concepts

Database Schema

- Structure of a database table

Old Schema:

id
title
description

New Schema:

id
title
description
category
status


## Why database.db was deleted

Changing table structure requires recreating the table.

This process is called:

Schema Reset

Common during development.


## New SQL Concept

INSERT INTO complaints
(title, description, category, status)

VALUES (?, ?, ?, ?)

- Stores all complaint information in database


## Dynamic Rendering

Complaint Card Now Shows:

- Category
- Status
- Title
- Description

Example:

[Infrastructure]   [Pending]

Broken Fan

Fan not working in Block B


## New CSS Concepts

display: flex

- Places elements side-by-side

justify-content: space-between

- Pushes items to opposite ends

border-radius: 20px

- Creates pill/badge shape


## UI Components Learned

Category Badge

Example:
Infrastructure

Status Badge

Example:
Pending


## Important Understanding

Good software stores structured information.

Instead of:

"Broken fan"

The system now knows:

Title:
Broken Fan

Category:
Infrastructure

Status:
Pending

Description:
Fan not working in room 203


## Commands Used

python app.py
- Run Flask app

git add .
- Stage changes

git commit -m "Added categories and status system"
- Save checkpoint

git push
- Upload changes to GitHub


## Day 6 Result

- Complaints categorized
- Status tracking introduced
- Database structure improved
- Project moved closer to a real issue-management system