from langchain_huggingface import HuggingFaceEndpoint
from prompts.score_prompt import score_prompt

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.4,
    max_new_tokens=300
)

def score_chain(match_data):
    return (score_prompt | llm).invoke({
        "match_data": match_data
    })