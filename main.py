from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import mysql.connector
from mysql.connector import Error
import bcrypt  # Import bcrypt for password hashing
from pydantic import BaseModel, Field  # Import BaseModel for validating request body

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="admin",
    database="test",
)
cursor = db.cursor(buffered=True)

# Create a 'users' table
try:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    print("Table 'users' created successfully")

except Error as e:
    print(f"Error: {e}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Check username and password (implement your authentication logic)
    cursor.execute(
        "select * from users where username = %s and password = %s",
        (username, password),
    )
    user = cursor.fetchone()

    # If authenticated, render the page for adding a new user
    if user:
        return templates.TemplateResponse(
            "add_user.html", {"request": request, "username": username}
        )
    else:
        return templates.TemplateResponse(
            "error.html", {"request": request, "message": "Invalid credentials!"}
        )


@app.get("/add_user", response_class=HTMLResponse)
async def add_user_page(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})


@app.post("/add_user", response_class=HTMLResponse)
async def add_user(
    request: Request, new_username: str = Form(...), new_password: str = Form(...)
):
    # Try adding a new user to the database
    try:
        cursor.execute(
            "insert into users (username, password) values (%s, %s)",
            (new_username, new_password),
        )
        db.commit()
        return templates.TemplateResponse(
            "success.html", {"request": request, "message": "User added successfully!"}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "error.html", {"request": request, "message": f"Error: {e}"}
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
