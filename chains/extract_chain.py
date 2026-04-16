from langchain_huggingface import HuggingFaceEndpoint
from prompts.extract_prompt import extract_prompt

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.4,
    max_new_tokens=300
)

def extract_chain(resume):
    return (extract_prompt | llm).invoke({"resume": resume})