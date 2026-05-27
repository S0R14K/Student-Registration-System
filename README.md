# Student Registration System

A university course project web application for managing student registrations, built with Python, Flask, SQLAlchemy, SQLite, Flask-WTF, and Bootstrap 5.

**Author:** Nikoloz Jigania  
**Course:** Software Engineering

## Features

- Student management: create, view, edit, and delete students
- Lecturer management: create, view, edit, and delete lecturers
- Course management: create, view, edit, and delete courses
- Enrollment management: register students in courses and drop enrollments
- Dashboard with summary statistics
- Search for students, lecturers, and courses
- Form validation and duplicate enrollment prevention
- Flash messages for success and error feedback

## Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3 |
| Web Framework | Flask |
| ORM | SQLAlchemy |
| Database | SQLite |
| Forms | Flask-WTF / WTForms |
| Templates | Jinja2 |
| CSS Framework | Bootstrap 5 |

## Project Structure

```text
student_registration_system/
|-- app.py
|-- config.py
|-- models.py
|-- forms.py
|-- init_db.py
|-- seed_data.py
|-- requirements.txt
|-- README.md
|-- diagrams/
|-- screenshots/
|-- static/
|   |-- css/
|   |   `-- style.css
|   `-- js/
|       `-- script.js
`-- templates/
    |-- base.html
    |-- index.html
    |-- students/
    |-- lecturers/
    |-- courses/
    `-- enrollments/
```

## Setup and Run

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create the database tables:

   ```powershell
   python init_db.py
   ```

4. Add sample lecturers and courses:

   ```powershell
   python seed_data.py
   ```

5. Run the application:

   ```powershell
   python app.py
   ```

6. Open the app:

   ```text
   http://127.0.0.1:5000
   ```

## UML Diagrams and Screenshots

The project includes PNG files in:

- `diagrams/`
- `screenshots/`

## Entity Relationships

- Student 1 to many Enrollment
- Course 1 to many Enrollment
- Lecturer 1 to many Course

## Iterations

| Iteration | Scope |
| --- | --- |
| 1 | Student, lecturer, and course CRUD |
| 2 | Enrollment functionality and validation |
| 3 | Dashboard, search, flash messages, screenshots, diagrams, and UI cleanup |

## License

This project is for educational purposes only.
