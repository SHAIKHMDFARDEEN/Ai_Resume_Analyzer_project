from openai import OpenAI
import json
import os

def analyze_resume(resume_text, user_goal):
    api_key = os.environ.get("OPENAI_API_KEY") or "sk-your-actual-openai-api-key"

    # If you don't have an OpenAI key yet, return mock data for testing
    if not api_key or api_key == "sk-your-actual-openai-api-key":
        return {
            "skills": ["Python", "Flask", "SQLAlchemy", "Git", "REST APIs"],
            "missing_skills": ["Docker", "Kubernetes", "Redis", "Unit Testing"],
            "roadmap": [
                "Master Flask advanced patterns and authentication",
                "Learn Redis caching and Celery task queues",
                "Containerize your app using Docker",
                "Practice system design interview questions"
            ],
            "Roadmap": [
                "Master Flask advanced patterns and authentication",
                "Learn Redis caching and Celery task queues",
                "Containerize your app using Docker",
                "Practice system design interview questions"
            ],
            "interview_questions": [
                "How does SQLAlchemy handle database sessions and pooling?",
                "What is the difference between GET and POST in Flask?",
                "How do you secure user passwords before storing them in MySQL?",
                "How do you optimize slow SQL queries in a production app?"
            ]
        }

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal: "{user_goal}"

STRICT RULES:
- Extractonly relevant skills for this goal
- REMOVE irrelevant tools [excel for backend, etc]
- Identify real gaps
- Generate roadmap only for missing fields
- Make output DIFFERENT based on goal

Return only JSON:
{{
"skills":[],
"missing_skills": [],
"roadmap": [],
"interview_questions":[]
}}

Resume:
{resume_text}
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You're a strict hiring manager."},
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        data = json.loads(content[start:end])
        if "roadmap" in data and "Roadmap" not in data:
            data["Roadmap"] = data["roadmap"]
        return data

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "Roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }
