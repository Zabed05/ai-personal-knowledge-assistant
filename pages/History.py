import streamlit as st

from utils.database import (
    get_chat_history,
    get_all_documents
)
from utils.session import initialize_session


# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="History | Gyanibaba",
    page_icon="📜",
    layout="wide"
)

initialize_session()

# ---------------------------------
# Hero Section
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
📜 Chat History
</h1>

<p style="font-size:18px;">
View previous conversations for each uploaded document.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------
# Load Documents
# ---------------------------------
documents = get_all_documents()

if not documents:
    st.info("No documents uploaded yet.")
    st.stop()

document_names = [
    doc["file_name"]
    for doc in documents
]

document_ids = [
    doc["id"]
    for doc in documents
]

selected_name = st.selectbox(
    "📚 Select Document",
    document_names
)

selected_index = document_names.index(selected_name)
selected_document_id = document_ids[selected_index]


# ---------------------------------
# Load History
# ---------------------------------
history = get_chat_history(selected_document_id)

if not history:

    st.info("No chat history found for this document.")

else:

    st.success(
        f"{len(history)} conversation(s) found."
    )

    for chat in history:

        with st.expander(
            f"Conversation #{chat['id']}"
        ):

            st.markdown("### 👤 User")
            st.write(chat["user_message"])

            st.markdown("### 🤖 Gyanibaba")
            st.write(chat["ai_response"])

            if chat.get("created_at"):
                st.caption(
                    f"🕒 {chat['created_at']}"
                )