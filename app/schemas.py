from pydantic import BaseModel


class UserInput(BaseModel):
    name: str
    user_id: str
    age: int
    weight: float
    fitness_goal: str
    intensity: str


class FeedbackInput(BaseModel):
    user_id: str
    feedback: str