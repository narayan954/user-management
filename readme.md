# FastAPI-MySQL-Authentication

This is a simple FastAPI project demonstrating user authentication with MySQL database integration.

## Features

- User login with authentication
- Adding new users to the database

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- MySQL server
- Virtual environment (optional but recommended)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-mysql-authentication.git
   ```

2. Navigate to the project directory:

   ```bash
   cd {project-directory}
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure MySQL:
   
   Create a MySQL database and update the connection details in main.py:

   ```python
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
    ```

6. Run the application to create the 'users' table in the database.
    
    ```bash
    uvicorn main:app --reload
    ```

7. Stop the application and add a new user to the database by uncommenting the following lines in main.py:

    ```python
    # from database import create_user
    # create_user("username", "password")
    ```
    Run the application again to add the new user to the database.

    ```bash
    uvicorn main:app --reload
    ```
    Stop the application and comment out the lines again.

8. Run the application again and visit  http://127.0.0.1:8000 in your browser to access the login page.
   Use the provided login credentials or add new users through the application.

9. Test Credential Example:

    ```bash
    username: testuser
    password: testpassword
    ```