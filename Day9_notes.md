# Day 9 Notes – CRUD

## CRUD

C → Create

R → Read

U → Update

D → Delete

---

## CampusPulse CRUD

Create
- Student submits complaint

Read
- View all complaints

Update
- Change complaint status

Delete
- Remove complaint

---

## SQL Commands

INSERT INTO
- Create

SELECT
- Read

UPDATE
- Modify existing data

DELETE
- Remove existing data

---

## Flask Routes

POST /submit
- Create

GET /complaints
- Read

GET /resolve/<id>
- Update

GET /delete/<id>
- Delete

---

## New Flask Concept

redirect()

Used to navigate user to another page after completing an operation.

---

## New SQL Concept

WHERE

Targets a specific row.

Example:

WHERE id = 5

Only complaint 5 is affected.

---

## Important Understanding

Almost every web application is a CRUD application.

Learning CRUD means learning the foundation of real-world software.

---

## Day 9 Result

- Understood CRUD
- Added Update functionality
- Added Delete functionality (optional)
- Learned SQL UPDATE and DELETE
- Project became a complete CRUD application