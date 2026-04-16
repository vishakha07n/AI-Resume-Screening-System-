from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following from the resume:

- Skills
- Experience
- Tools

STRICT RULES:
- Do NOT add extra text
- Do NOT assume missing skills
- Keep output clean

Resume:
{resume}
"""
)