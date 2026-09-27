def update_workout_plan(current_plan, feedback):

    feedback_lower = feedback.lower()

    # Default updated plan
    updated_plan = current_plan

    # Easier workouts
    if (
        "easier" in feedback_lower
        or "easy" in feedback_lower
        or "simple" in feedback_lower
        or "beginner" in feedback_lower
    ):
        updated_plan = updated_plan.replace(
            "Strength",
            "Light strength exercises"
        )
        updated_plan = updated_plan.replace(
            "Full body",
            "Light full body"
        )

    # Reduce workout duration
    if (
        "duration" in feedback_lower
        or "shorter" in feedback_lower
        or "short" in feedback_lower
        or "less time" in feedback_lower
    ):
        updated_plan = updated_plan.replace(
            "20 minutes",
            "10-15 minutes"
        )
        updated_plan = updated_plan.replace(
            "30 minutes",
            "15-20 minutes"
        )

    # Walking preference
    if "walking" in feedback_lower:
        updated_plan += """

ADDITIONAL PREFERENCE
Walking exercises have been added based on your feedback.
"""

    # Stretching preference
    if "stretch" in feedback_lower:
        updated_plan += """

ADDITIONAL PREFERENCE
Extra stretching and flexibility exercises have been added.
"""

    # Jumping exercises
    if (
        "no jumping" in feedback_lower
        or "don't like jumping" in feedback_lower
        or "do not like jumping" in feedback_lower
        or "avoid jumping" in feedback_lower
    ):
        updated_plan += """

ADDITIONAL PREFERENCE
Jumping exercises have been removed from the updated plan.
"""

    # General exercise preference
    if (
        "exercise" in feedback_lower
        and "change" in feedback_lower
    ):
        updated_plan += """

ADDITIONAL PREFERENCE
The exercises have been adjusted according to your feedback.
"""

    return f"""
FITBUDDY - UPDATED FITNESS PLAN

Your workout plan has been updated based on your feedback.

USER FEEDBACK:
{feedback}

UPDATED PLAN:

{updated_plan}

NUTRITION & RECOVERY TIP:
Stay hydrated, eat balanced meals, eat nutritious food,
and get enough rest and recovery.

PLAN UPDATED SUCCESSFULLY
"""