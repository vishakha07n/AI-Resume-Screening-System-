from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_desc"],
    template="""
Compare the resume with job description.

Rules:
- Do NOT assume missing skills
- Only use provided data

Return:
- matched_skills
- missing_skills

Resume Data:
{resume_data}

Job Description:
{job_desc}
"""
)