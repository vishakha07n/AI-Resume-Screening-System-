from langchain_huggingface import HuggingFaceEndpoint
from prompts.match_prompt import match_prompt

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.4,
    max_new_tokens=300
)

def match_chain(resume_data, job_desc):
    return (match_prompt | llm).invoke({
        "resume_data": resume_data,
        "job_desc": job_desc
    })