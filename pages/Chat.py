import streamlit as st

from utils.session import initialize_session
from utils.database import (
    save_chat,
    get_latest_document,
    get_all_documents,
    get_document_by_id
)
from utils.gemini import get_ai_response
from utils.prompts import build_prompt


# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Chat | Gyanibaba",
    page_icon="💬",
    layout="wide"
)

initialize_session()

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True


# ---------------------------------
# Load Documents
# ---------------------------------
documents = get_all_documents()
st.session_state.documents = documents


# ---------------------------------
# Restore Default Document
# ---------------------------------
if (
    st.session_state.selected_document_id is None
    and documents
):
    latest = get_latest_document()

    if latest:
        st.session_state.selected_document_id = latest["id"]


# ---------------------------------
# Sidebar - Document Selection
# ---------------------------------
if documents:

    document_names = [
        doc["file_name"]
        for doc in documents
    ]

    document_ids = [
        doc["id"]
        for doc in documents
    ]

    if st.session_state.selected_document_id in document_ids:
        default_index = document_ids.index(
            st.session_state.selected_document_id
        )
    else:
        default_index = 0

    selected_name = st.sidebar.selectbox(
        "📚 Select Document",
        document_names,
        index=default_index
    )

    selected_index = document_names.index(selected_name)
    selected_document_id = document_ids[selected_index]

    if (
        selected_document_id
        != st.session_state.selected_document_id
    ):

        st.session_state.selected_document_id = selected_document_id
        st.session_state.messages = []

    document = get_document_by_id(
        st.session_state.selected_document_id
    )

    if document:

        st.session_state.pdf_content = document["document_text"]
        st.session_state.uploaded_file_name = document["file_name"]


# ---------------------------------
# Hero
# ---------------------------------
st.markdown("""
<style>

.hero{
    background: linear-gradient(135deg,#2563EB,#7C3AED);
    padding:18px 25px;
    border-radius:16px;
    text-align:center;
    color:white;
    margin-bottom:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1 style="margin-bottom:8px;">
🧠 Gyanibaba AI
</h1>

<p style="font-size:18px;">
Ask questions • Get instant answers • Learn smarter
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------
# Check Document
# ---------------------------------
if not st.session_state.pdf_content:

    st.warning("⚠ Please upload at least one PDF.")
    st.stop()


# ---------------------------------
# Current Document
# ---------------------------------
left, right = st.columns([8, 2])

with left:

    st.success(
        f"📄 **Current Document:** {st.session_state.uploaded_file_name}"
    )

with right:

    clear = st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
        disabled=len(st.session_state.messages) == 0
    )

if clear:

    st.session_state.messages = []
    st.rerun()


st.divider()


# ---------------------------------
# Welcome
# ---------------------------------
if (
    st.session_state.show_welcome
    and not st.session_state.messages
):

    st.info("""
### 👋 Welcome!

Try asking:

- Summarize this document
- Explain chapter 2
- Important interview questions
- Create MCQs
""")

    st.session_state.show_welcome = False


# ---------------------------------
# Previous Messages
# ---------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------
# Chat Input
# ---------------------------------
question = st.chat_input(
    "Ask anything about the selected document..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    prompt = build_prompt(
        st.session_state.pdf_content,
        st.session_state.messages,
        question
    )

    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):

            answer = get_ai_response(prompt)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    save_chat(
        st.session_state.selected_document_id,
        question,
        answer
    )