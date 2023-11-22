from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import mysql.connector

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
cursor = db.cursor()

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

finally:
    # Close the database connection
    if db.is_connected():
        cursor.close()
        db.close()
        print("Connection closed")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


"""
select * from users where username = 'admin' and password = 'admin'
"""


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
        return {"message": "Invalid Credentials"}


@app.post("/add_user", response_class=HTMLResponse)
async def add_user(
    request: Request, new_username: str = Form(...), new_password: str = Form(...)
):
    # Add a new user to the database (implement your logic)
    return {"message": "User added successfully!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
