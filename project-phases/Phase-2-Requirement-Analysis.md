# Phase 2 – Requirement Analysis

## Project Title

FitBuddy – AI-Based Personalized Fitness Assistant

## Functional Requirements

The FitBuddy system should provide the following functionalities:

1. Generate structured 7-day workout plans.
2. Provide concise and actionable nutrition tips.
3. Update workout plans based on user feedback.
4. Support real-time interaction with the user.
5. Accept the required user information for generating personalized fitness guidance.
6. Display the generated AI response to the user.

## User Requirements

The system should use the user's fitness-related information to provide personalized assistance.

The relevant information includes:

* Age
* Weight
* Fitness goal
* Workout intensity

## AI Requirements

The selected Generative AI solution should be capable of:

* Generating structured workout plans.
* Providing nutrition guidance.
* Updating plans based on user feedback.
* Producing useful responses from user-provided information.

## Technology Requirements

The project uses:

* Python
* FastAPI
* HTML
* CSS
* JavaScript
* Gemini API

## Expected System Behaviour

The user provides the required fitness information. The application sends the relevant information to the AI system, receives the generated response, and displays the personalized fitness guidance to the user.

## Error Handling Requirement

The application should handle situations such as unavailable AI services or API connection problems and provide an appropriate message to the user instead of failing without explanation.
