from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from pydantic import BaseModel  
from starlette.status import HTTP_303_SEE_OTHER
import jwt  
import os
import time

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "WRONG_KEY")  # set an env var in real use
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(payload: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    to_encode = payload.copy()
    to_encode["exp"] = int(time.time()) + ACCESS_TOKEN_EXPIRE_MINUTES * 60
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


app = FastAPI()

# Simple welcome endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your first FastAPI app 🎉"}

# serve the login HTML page
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/login", response_class=HTMLResponse)
def serve_login_page():
    return read_file("web/login.html")


@app.post("/api/login")
def login(payload: dict):
    """
    Accepts JSON:
      { "username": "admin", "password": "password" }
    Returns JSON with success/failure.
    """
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        # 400: client sent bad input
        raise HTTPException(status_code=400, detail="username and password are required")

    # DEMO check — hardcoded
    if username == "admin" and password == "password":
        # make a JWT
        token = create_access_token({"sub": username})

        resp = JSONResponse({"ok": True, "message": "Login successful"})

        resp.set_cookie(
            key="logged_in",
            value="yes",
            samesite="lax",
            secure=False,   # set True when you move to HTTPS in prod
            path="/"
        )

        # NEW: HttpOnly JWT cookie
        resp.set_cookie(
            key="access_token",
            value=token,
            httponly=True,     # JS cannot read this; safer
            samesite="lax",
            secure=False,      # set True when behind HTTPS
            max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            path="/",
        )
        
        return resp
        
    else:
        # 401: unauthorized
        raise HTTPException(status_code=401, detail="Invalid username or password")
    

@app.get("/data_entry", response_class=HTMLResponse)
def serve_app_page(request: Request):
    if request.cookies.get("logged_in") != "yes":
        # not logged in -> go to /login
        return RedirectResponse(url="/login", status_code=HTTP_303_SEE_OTHER)
    return read_file("web/data-entry.html")