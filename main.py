from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from users.models import User, UserCreate
import users.crud as crud

app = FastAPI(title="Backend Service Mon Assiette", version="0.1.0")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/register", response_model = User)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cette email est déjà utilisée.",
        )

    new_user = crud.create_user(db, user)

    return User(
        username=new_user.username,
        email=new_user.email,
        #full_name=new_user.full_name,
        disabled=not new_user.is_active,
    )