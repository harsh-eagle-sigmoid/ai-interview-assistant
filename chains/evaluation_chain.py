from langchain_core.prompts import ChatPromptTemplate

def evaluation_chain(llm):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a strict technical interviewer. Evaluate ONLY based on the candidate's answer."
        ),
        (
            "human",
            """Interview Question:
{question}

Candidate Answer:
{answer}

Instructions:
- Compare the answer with what a correct answer should include
- Identify what is correct and what is missing
- Base strengths and weaknesses ONLY on the candidate answer

Provide the evaluation in this format:

Score (out of 10):
Strengths:
Weaknesses:
How to Improve:
Sample Ideal Answer:
"""
        )
    ])
    return prompt | llm
