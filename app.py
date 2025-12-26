import streamlit as st
from utils.llm import load_llm
from chains.question_chain import question_chain
from chains.evaluation_chain import evaluation_chain

# Page config
st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    layout="centered"
)

st.title("🤖 AI Interview Preparation Assistant")

# Load LLM
with st.spinner("Loading AI model..."):
    llm = load_llm()

# Sidebar settings
with st.sidebar:
    st.header("Interview Settings")

    role = st.selectbox(
        "Select Job Role",
        [
            "Frontend Developer",
            "Backend Developer",
            "Python Developer",
            "Java Developer"
        ]
    )

    level = st.selectbox(
        "Select Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )

# Session state
if "question" not in st.session_state:
    st.session_state.question = ""

# Ask question
if st.button("Ask Interview Question"):
    with st.spinner("Generating interview question..."):
        q_chain = question_chain(llm)
        response = q_chain.invoke(
            {
                "role": role,
                "level": level
            }
        )
        st.session_state.question = response.content

# Display question
if st.session_state.question:
    st.subheader("📌 Interview Question")
    st.write(st.session_state.question)

    answer = st.text_area("✍️ Your Answer")

    if st.button("Evaluate Answer"):
        if not answer.strip():
            st.warning("Please enter an answer before evaluation.")
        else:
            with st.spinner("Evaluating your answer..."):
                e_chain = evaluation_chain(llm)
                response = e_chain.invoke(
                    {
                        "question": st.session_state.question,
                        "answer": answer
                    }
                )

                st.subheader("📊 Interview Feedback")
                st.write(response.content)
