from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE user
@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# READ users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
