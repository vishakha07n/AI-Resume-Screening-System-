### AI Resume Screening System (LangChain + Hugging Face + LangSmith)

## Project Overview
This project is an AI-powered Resume Screening System that evaluates candidates based on a given job description. It simulates a real-world recruiter workflow by extracting skills, matching them with job requirements, assigning a score, and providing an explanation.

## Objective
Automate resume evaluation using AI
Provide fit score (0–100)
Generate explainable results
Enable pipeline tracing using LangSmith

## Pipeline Architecture
```
Resume + Job Description
        ↓
[Skill Extraction]
        ↓
[Matching]
        ↓
[Scoring]
        ↓
[Explanation]
        ↓
Final Output + LangSmith Tracing
```

## Tech Stack
- Python
- LangChain (LCEL)
- Hugging Face API
- LangSmith (Tracing & Debugging)
- VS Code / Jupyter Notebook

## Project Structure
```
resume-screening/
│
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   ├── explain_prompt.py
│
├── chains/
│   ├── extract_chain.py
│   ├── match_chain.py
│   ├── score_chain.py
│   ├── explain_chain.py
│
├── sample_data.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Sample Input
- Job Description
Python
Machine Learning
Pandas, NumPy
SQL
Deep Learning

- Resumes Tested
Strong Candidate
Average Candidate
Weak Candidate

## Sample Output
```
 STRONG CANDIDATE

Extracted Data:
Skills: Python, ML, SQL...

Match Result:
Matched Skills: Python, ML
Missing Skills: None

Score:
90
```
## Explanation:
Candidate has strong alignment with job requirements...

## Features

✔ Skill Extraction using LLM
✔ Resume vs Job Matching
✔ Candidate Scoring (0–100)
✔ Explainable AI output
✔ Modular LangChain pipeline
✔ LangSmith tracing for debugging

## Prompt Engineering
Strict instructions to avoid hallucination
No assumption of missing skills
Structured outputs for consistency

## LangSmith Tracing
Tracks each pipeline step:
Extraction
Matching
Scoring
Explanation

## Future Improvements
Streamlit UI for frontend
JSON structured output
Database integration
Resume upload (PDF parsing)
Advanced scoring (weighted skills)

## Acknowledgement

Thanks to Innomatics Research Labs and mentor for guidance and support throughout this project.
