from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match_data"],
    template="""
Explain why this candidate received this score.

Include:
- Strengths
- Weaknesses
- Missing skills

STRICT RULES:
- Do NOT assume extra skills
- Keep explanation clear and concise

Score: {score}
Match Data: {match_data}
"""
)