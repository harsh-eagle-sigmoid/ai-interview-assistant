from langchain_core.prompts import ChatPromptTemplate

def question_chain(llm):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a professional technical interviewer."
        ),
        (
            "human",
            """Ask ONE {level}-level interview question for the role of {role}.

Rules:
- Ask only ONE question
- Match the role and difficulty
- Output ONLY the question
"""
        )
    ])
    return prompt | llm
