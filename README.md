# ToDo Backend

This project is a simple ToDo backend API built with Flask, SQLAlchemy, and Flask-Migrate. It supports CRUD operations 
for managing ToDo items and provides basic documentation of the API via the `/` route. This is a standard OpenAPI spec
swagger API.

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository** 

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
3. ***Install the Required Packages***

   ```bash
   pip install -r requirements.txt
   ```
Set Up Environment Variables

4. **Create a .env file in the root of the project with the following content:**

   ```plaintext
   FLASK_APP=app.py
   FLASK_ENV=development
   ```
## Initialize the Database
1. **Run the following commands to set up the database and apply migrations:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application
1. **To start the Flask development server, use the following command:**

   ```bash
   flask run
   ```

   The application will be accessible at http://127.0.0.1:5000.

## Unit Testing
1. **To run unit tests, use pytest. Ensure you have pytest installed, then run:**

   ```bash
   pip install pytest
   pytest
   ```
   Tests should be placed in the tests/ directory.

# Migrations
1. **For managing database schema changes, use Flask-Migrate. Commands include:**

   Create a new migration: 
   ```bash 
   flask db migrate -m "Description"
   ```

   Apply migrations: 
   ```bash 
   flask db upgrade
   ```

   Rollback migrations: 
   ```bash 
   flask db downgrade
   ```

## API Endpoints

Visit the running application at http://127.0.0.1:5000 to view API Documentation.