from fastapi import FastAPI, Depends
from app.auth import router as auth_router
from app.deps import get_current_user

app = FastAPI(title="Students API")

app.include_router(auth_router)


@app.get("/students")
def students(user=Depends(get_current_user)):
    return {"message": f"Hello {user}"}