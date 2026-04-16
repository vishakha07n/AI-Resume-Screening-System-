from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint
from prompts.explain_prompt import explain_prompt

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.4,
    max_new_tokens=300
)
def explain_chain(score, match_data):
    return (explain_prompt | llm).invoke({
        "score": score,
        "match_data": match_data
    })
