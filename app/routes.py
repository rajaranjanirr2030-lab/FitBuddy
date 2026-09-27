from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import User, WorkoutPlan
from .gemini_generator import generate_workout_plan
from .updated_plan import update_workout_plan


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# HOME PAGE
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


# GENERATE WORKOUT PLAN
@router.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    fitness_goal: str = Form(...),
    intensity: str = Form(...)
):
    db: Session = SessionLocal()

    plan = generate_workout_plan(
        name,
        age,
        weight,
        fitness_goal,
        intensity
    )

    user = User(
        name=name,
        user_id=user_id,
        age=age,
        weight=weight,
        fitness_goal=fitness_goal,
        intensity=intensity
    )

    db.add(user)

    workout = WorkoutPlan(
        user_id=user_id,
        plan=plan,
        nutrition_tip="Follow proper hydration, nutrition and recovery."
    )

    db.add(workout)

    db.commit()
    db.close()

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": name,
            "user_id": user_id,
            "plan": plan
        }
    )
# FEEDBACK PAGE
@router.get("/feedback", response_class=HTMLResponse)
def feedback_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="feedback.html",
        context={
            "request": request
        }
    )
# UPDATE WORKOUT PLAN
@router.post("/update", response_class=HTMLResponse)
def update(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    db: Session = SessionLocal()

    workout = (
        db.query(WorkoutPlan)
        .filter(WorkoutPlan.user_id == user_id)
        .order_by(WorkoutPlan.id.desc())
        .first()
    )

    if workout:

        # Save the original plan before updating
        original_plan = workout.plan

        # Generate updated plan based on feedback
        new_plan = update_workout_plan(
            original_plan,
            feedback
        )

        # Save updated plan
        workout.plan = new_plan
        workout.feedback = feedback

        db.commit()

        plan = new_plan

    else:
        original_plan = ""
        plan = "No workout plan found."

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": "User",
            "user_id": user_id,
            "plan": plan,
            "original_plan": original_plan,
            "feedback": feedback,
            "updated": True
        }
    )
# UPDATE USER STATUS
@router.post("/admin/update-status", response_class=HTMLResponse)
def update_status(
    request: Request,
    user_id: str = Form(...),
    status: str = Form(...)
):
    db: Session = SessionLocal()

    user = (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )

    if user:
        user.status = status
        db.commit()

    users = db.query(User).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={
            "request": request,
            "users": users
        }
    )
# ADMIN - ALL USERS
@router.get("/admin", response_class=HTMLResponse)
def admin(request: Request):
    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={
            "request": request,
            "users": users
        }
    )