from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(String, unique=True)
    age = Column(Integer)
    weight = Column(Float)
    fitness_goal = Column(String)
    intensity = Column(String)
    status = Column(String, default="New")


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    plan = Column(Text)
    nutrition_tip = Column(Text)
    feedback = Column(Text, nullable=True)