# Trello Backend API

This project is a backend API built with FastAPI for managing boards, sections, tickets, and team collaboration through invitation links. It was designed to simulate the core functionality of tools like Trello while following clean backend architecture principles.

The application uses JWT authentication, PostgreSQL for data storage, and a modular structure based on Routes → Services → Repositories.

---

## What This Project Can Do

* Register new users
* Secure user login with JWT tokens
* Create and manage boards
* Organize boards into sections
* Create, update, move, and delete tickets
* Invite other users to collaborate on boards
* Apply permission rules for owners and members
* Provide interactive API documentation with Swagger

---

## Tech Stack

This project was built using:

* Python 3
* FastAPI
* SQLAlchemy
* PostgreSQL
* Passlib (password hashing)
* Python-JOSE (JWT authentication)
* Uvicorn

---

## Project Structure

```text id="m4q8vk"
app/
├── api/
│   └── v1/
│       └── routes/
├── services/
├── repositories/
├── dependencies/
├── models/
├── schemas/
├── core/
├── db/

main.py
requirements.txt
README.md
.env.example
```

The project follows a layered architecture so that business logic, database logic, and API routes stay clean and easy to maintain.

---

# How to Run This Project Locally

## 1. Clone the Repository

```bash id="x7p2lc"
git clone <your-repository-url>
cd <your-project-folder>
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash id="p5n1tb"
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash id="u6r3mk"
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Required Packages

```bash id="k9m4zx"
pip install -r requirements.txt
```

---

## 4. Create a PostgreSQL Database

Create a database locally. Example:

```text id="g2v7lc"
trello_db
```

---

## 5. Add Environment Variables

Create a file named:

```text id="r8p1qc"
.env
```

Then add:

```env id="t3m6zb"
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
TOKEN_EXPIRATION=60
DATABASE_URL=postgresql://username:password@localhost:5432/trello_db
```

Example:

```env id="f1n7lc"
DATABASE_URL=postgresql://postgres:1234@localhost:5432/trello_db
```

---

## 6. Start the Server

```bash id="m2q7vk"
uvicorn main:app --reload
```

Once running, the API will be available locally.

---

## 7. Open API Docs

Visit:

```text id="x4p8lc"
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test endpoints directly in the browser.

---

# Authentication Guide

1. Register a user using:

```text id="n7p2lc"
POST /register
```

2. Login using:

```text id="p4r8lk"
POST /login
```

3. Copy the JWT token returned by the login endpoint.

4. In Swagger Docs, click **Authorize**.

5. Paste:

```text id="g5r1tv"
Bearer your_token_here
```

You can now access protected routes.

---

# Main API Endpoints

## Authentication

* POST `/register`
* POST `/login`

## Boards

* POST `/boards`
* GET `/boards`
* GET `/boards/{board_id}`

## Sections

* POST `/boards/{board_id}/sections`
* GET `/boards/{board_id}/sections`
* PUT `/sections/{section_id}`
* DELETE `/sections/{section_id}`

## Tickets

* POST `/sections/{section_id}/tickets`
* GET `/sections/{section_id}/tickets`
* PUT `/tickets/{ticket_id}`
* DELETE `/tickets/{ticket_id}`

## Invitations

* POST `/boards/{board_id}/invite`
* POST `/invitations/{token}/accept`

---

# Permission Rules

## Board Owner

The board owner has full control and can:

* Manage boards
* Create, edit, and delete sections
* Manage all tickets
* Invite other users

## Board Members

Invited members can:

* Access shared boards
* Work only on tickets they created themselves

---

# Notes for Development

* Keep secrets inside `.env`
* Do not upload `.env` to GitHub
* Do not upload local databases or tokens
* Use `.gitignore` properly

---

## Testing Guide

This project includes both **unit tests** and **integration tests** to ensure reliability and correctness.

---

### Test Types

#### 1. Unit Tests

* Focus on **business logic (service layer)**
* Do NOT use real database
* Use **mock/fake repositories**
* Example:

  * AuthService
  * BoardService
  * TicketService

---

#### 2. Integration Tests

* Test **full API flow**
* Use FastAPI `TestClient`
* Include:

  * Register → Login → Token → API calls
* Example:

  * `/login`
  * `/boards`
  * `/sections`
  * `/tickets`

---

### Run All Tests

```bash
PYTHONPATH=. pytest
```

---

### Run Tests with Coverage

```bash
PYTHONPATH=. pytest --cov=app
```

---

### Current Coverage

```text
TOTAL: 85%
```

✔ Requirement: At least 50%
✔ Achieved: 85%

---

### Test Structure

```text
tests/
  unit/
    test_auth_service.py
    test_board_service.py
    test_ticket_service.py

  integration/
    test_auth.py
```

---

### Key Testing Concepts Used

* Dependency Injection
* Mocking repositories
* Isolating business logic
* Token-based authentication testing
* End-to-end API validation

---

### Notes

* Each test is **independent**
* Unique data is used (UUID) to avoid conflicts
* No real production data is used


# Author

Sandeep Tekkali
