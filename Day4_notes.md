# Day 4 Notes

## Goal of Day 4

Store complaints permanently using SQLite database.


## What Changed Today

Before:
- complaint data disappeared after refresh/restart

Now:
- complaint data stored permanently in database


## SQLite

SQLite is a lightweight file-based database.

Database file:
database.db


## Database Concepts Learned

Table
- stores structured data

Row
- one complaint entry

Column
- specific field like title or description


## SQL Commands Learned

CREATE TABLE
- creates database table

INSERT INTO
- stores data into table

SELECT * FROM
- retrieves all data


## Python Database Concepts

sqlite3.connect()
- connects Python to database

cursor.execute()
- runs SQL query

conn.commit()
- saves database changes

conn.close()
- closes database connection


## New Flask Flow

User submits complaint
→ Flask receives data
→ SQLite stores data
→ Flask retrieves data
→ complaints displayed dynamically


## New Route Added

/complaints

- displays all stored complaints


## Jinja Template Concepts

{% for complaint in complaints %}
- loops through complaints list

{{ complaint[1] }}
- displays complaint title

{{ complaint[2] }}
- displays complaint description


## Important Understanding

Frontend:
- HTML form collects data

Backend:
- Flask processes data

Database:
- SQLite stores data permanently


## Commands Used

python app.py
- runs Flask app

git add .
- stages changes

git commit -m "message"
- creates checkpoint

git push
- uploads changes to GitHub


## Day 4 Result

- database connected successfully
- complaints stored permanently
- complaints displayed dynamically
- first real backend persistence implemented