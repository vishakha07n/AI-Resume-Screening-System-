from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Give a score (0-100) based on skill match.

Rules:
- More matched skills → higher score
- Missing critical skills → reduce score

Return only number.

Match Data:
{match_data}
"""
)