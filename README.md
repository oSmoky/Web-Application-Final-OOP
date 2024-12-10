# Web-Application-Final-OOP
University Schedule Management System

{This project is a web application for managing and displaying course information from a PostgreSQL database.
It includes a backend built with Python (using Flask) and a frontend designed with HTML and CSS.}

1)Project Overview
The application allows users to:
- View course details such as course name, code, description, level (Undergraduate/Graduate), and credits.
- Filter courses by their level.
- Write and store personal notes directly on the webpage.

2)Technologies Used
- Backend: Flask (Python) with SQLAlchemy for database interaction.
- Frontend: HTML, CSS, and JavaScript.
- Database: PostgreSQL for storing course details.

[Database Setup]
- Create the Database:
Run SQL command in your application (e.g. DBeaver)

"CREATE DATABASE universitySchedule;" *if not exist database name*

- Create the Table
*Depends what you want to add in your project*

"CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    location TEXT,
    level VARCHAR(20),
    credits INTEGER
);"

- Insert Data: e.g.

"INSERT INTO courses (code, name, location, level, credits) VALUES
('COSC 1550', 'Computer Programming I', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 3),
('COSC 1570', 'Mathematics for Computer Science', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 3),
('POLT 1070', 'Introduction to Political Theory', 'Webster Univ Tashkent, Uzbekistan', 'Graduate', 3),
('MATH 1610', 'Calculus I', 'Webster Univ Tashkent, Uzbekistan', 'Graduate', 5),
('COSC 3050', 'Data Structures I', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 4);"

3) Application setup

- Install Dependencies e.g. in PyCharm console:
*or other libraries depends on what library you use*

"pip install flask flask_sqlalchemy psycopg2"

Author - Asilxon Maksumov - Computer Science Major
