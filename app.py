import streamlit as st

from utils.session import initialize_session
from utils.database import (
    get_latest_document,
    get_document_by_id,
    get_all_documents
)

# ---------------------------------------
# Page Config
# ---------------------------------------
st.set_page_config(
    page_title="Gyanibaba",
    page_icon="🧠",
    layout="wide"
)

initialize_session()

# ---------------------------------------
# Restore Current Document
# ---------------------------------------
if st.session_state.selected_document_id:

    document = get_document_by_id(
        st.session_state.selected_document_id
    )

    if document:

        st.session_state.uploaded_file_name = document["file_name"]
        st.session_state.pdf_content = document["document_text"]

else:

    latest_document = get_latest_document()

    if latest_document:

        st.session_state.selected_document_id = latest_document["id"]
        st.session_state.uploaded_file_name = latest_document["file_name"]
        st.session_state.pdf_content = latest_document["document_text"]


# ---------------------------------------
# Get Dashboard Data
# ---------------------------------------
documents = get_all_documents()

total_documents = len(documents)

current_document = st.session_state.uploaded_file_name


# ---------------------------------------
# Custom CSS
# ---------------------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:800;
    color:white;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:#E5E7EB;
}

.hero{
    background:linear-gradient(135deg,#2563EB,#7C3AED);
    padding:40px;
    border-radius:18px;
    margin-bottom:25px;
}

.feature-card{
    background:#262730;
    border-radius:15px;
    padding:25px;
    border:1px solid #3b3b3b;
    height:230px;
}

.feature-title{
    font-size:22px;
    font-weight:bold;
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------
# Hero
# ---------------------------------------
st.markdown("""
<div class="hero">

<div class="main-title">
🧠 Gyanibaba
</div>

<div class="sub-title">
AI Personal Knowledge Assistant
<br><br>
Upload PDFs • Chat with Gemini • Store Knowledge
</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------
# Features
# ---------------------------------------
st.subheader("✨ What You Can Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="feature-card">

<div class="feature-title">
📄 Upload PDFs
</div>

Upload one or more study notes,
books, manuals or reports.

Extract text automatically
and build your knowledge base.

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature-card">

<div class="feature-title">
🤖 AI Chat
</div>

Select any uploaded document
and ask questions using
Google Gemini AI.

Get instant answers.

</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="feature-card">

<div class="feature-title">
📜 Chat History
</div>

Every conversation is
saved in MySQL.

Review previous chats anytime.

</div>
""", unsafe_allow_html=True)

st.write("")


# ---------------------------------------
# Dashboard
# ---------------------------------------
st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:

    if current_document:

        st.metric(
            "Current Document",
            "Loaded ✅"
        )

    else:

        st.metric(
            "Current Document",
            "None"
        )

with col2:

    st.metric(
        "Uploaded PDFs",
        total_documents
    )

with col3:

    st.metric(
        "AI Model",
        "Gemini"
    )

st.write("")


# ---------------------------------------
# Current Document
# ---------------------------------------
st.subheader("📄 Current Document")

if current_document:

    st.success(f"**{current_document}**")

    if st.session_state.pdf_content:

        st.info(
            f"Characters: {len(st.session_state.pdf_content):,}"
        )

else:

    st.warning("No PDF uploaded yet.")

st.write("")


# ---------------------------------------
# Footer
# ---------------------------------------
st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit • Google Gemini • MySQL

<b>Version 2.0 - by ZKAHM</b>

</div>
""", unsafe_allow_html=True)