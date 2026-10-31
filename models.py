from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import synonym
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    resume_text = Column(Text)
    result = Column(Text)

    # Synonyms so both singular and plural names work
    results = synonym("result")
    resume = synonym("resume_text")

# Alias so both models.Report and models.Reports work
Report = Reports
