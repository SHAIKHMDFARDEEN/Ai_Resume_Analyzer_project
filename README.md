# 🚀 AI Resume Analyzer & Career Copilot

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![TiDB Cloud](https://img.shields.io/badge/TiDB%20Cloud-Serverless%20MySQL-F32B56?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge)

An intelligent, full-stack AI Career Copilot web application built with **Python**, **Flask**, **OpenAI API**, and **TiDB Cloud Serverless MySQL**. The application parses resumes in multiple formats (PDF, DOCX, and raw text), provides deep structural feedback using LLMs, calculates ATS match scores, identifies skill gaps, and persists analysis history across user sessions.

---

## 🌟 Key Features

- **Multi-Format Ingestion**: Upload resumes seamlessly as **PDF** (via `PyPDF2`), **DOCX** (via `python-docx`), or paste raw text.
- **AI-Powered Deep Evaluation**:
  - **Overall ATS Score**: Match score based on industry standards.
  - **Summary & Profile Evaluation**: High-level candidate assessment.
  - **Identified Strengths**: Key technical and domain advantages.
  - **Areas for Improvement**: Actionable suggestions to enhance hiring appeal.
  - **Skill Gap Analysis**: Identifies missing keywords and complementary competencies.
  - **Recommended Action Items**: Step-by-step guidance to optimize the resume.
- **TiDB Cloud Serverless MySQL**:
  - Cloud-native relational database connected via TLS/SSL.
  - Securely stores user profiles and historical resume reports.
- **Authentication & User Management**:
  - Complete sign-up, sign-in, and session management system.
  - History tracking so users can review past resume evaluations at any time.
- **Modern Responsive UI**:
  - Clean, elegant interface built with semantic HTML5, Jinja2 templates, and custom CSS3.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | [Flask](https://flask.palletsprojects.com/) (Python 3.13) |
| **Database** | [TiDB Cloud](https://tidbcloud.com/) Serverless MySQL |
| **ORM / Data Access** | [SQLAlchemy](https://www.sqlalchemy.org/) & [PyMySQL](https://pymysql.readthedocs.io/) with TLS/SSL |
| **AI Model** | [OpenAI](https://platform.openai.com/) GPT-4o-mini |
| **Document Parsers** | [PyPDF2](https://pypdf2.readthedocs.io/) & [python-docx](https://python-docx.readthedocs.io/) |
| **Frontend** | HTML5, CSS3, Jinja2 Templates |

---

## 📂 Project Structure

```text
AI_RESUME_PROJECT/
├── static/
│   └── style.css            # Custom responsive styles
├── templates/
│   ├── base.html            # Core layout & navigation
│   ├── login.html           # Authentication login page
│   ├── signup.html          # User registration page
│   ├── dashboard.html       # Resume upload & analysis view
│   └── history.html         # User analysis history view
├── ai.py                    # OpenAI integration & prompt engineering
├── app.py                   # Flask routing & application controller
├── db.py                    # TiDB Cloud engine & SQLAlchemy session
├── models.py                # Database schemas (User, Report)
├── requirements.txt         # Project dependencies
└── .gitignore               # Ignored environments & cache
```

---

## 🚀 Getting Started Locally

### 1. Clone the repository:
```bash
git clone https://github.com/SHAIKHMDFARDEEN/Ai_Resume_Analyzer_project.git
cd Ai_Resume_Analyzer_project
```

### 2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables:
Set up your OpenAI API key and TiDB Cloud connection credentials:
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-openai-api-key"

# Linux / macOS
export OPENAI_API_KEY="your-openai-api-key"
```

### 5. Initialize the Database & Run:
```bash
# Create database tables
python models.py

# Launch the Flask application
python app.py
```

Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## 📈 Roadmap & Future Enhancements

- [ ] Job Description (JD) matching for targeted role comparison.
- [ ] Export evaluated resume reports as formatted PDF downloads.
- [ ] Direct LinkedIn profile scraping & review.
- [ ] Automated resume rewriting suggestions with 1-click apply.

---

## 👨‍💻 Author

**Mohammed Fardeen**  
- GitHub: [@SHAIKHMDFARDEEN](https://github.com/SHAIKHMDFARDEEN)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
