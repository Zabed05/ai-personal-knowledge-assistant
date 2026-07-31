import os
import streamlit as st

from config import UPLOAD_FOLDER
from utils.database import (
    save_document,
    get_all_documents
)
from utils.pdf_reader import extract_text
from utils.session import initialize_session


# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Upload | Gyanibaba",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------
# Initialize Session
# ---------------------------------
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
📄 Upload Documents
</h1>

<p style="font-size:18px;">
Upload one or more PDFs to build your personal knowledge base.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------
# Upload Section
# ---------------------------------
uploaded_files = st.file_uploader(
    "Choose PDF file(s)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    progress = st.progress(0)

    total_files = len(uploaded_files)

    for index, uploaded_file in enumerate(uploaded_files):

        with st.spinner(f"Processing {uploaded_file.name}..."):

            file_path = os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            )

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            pdf_text = extract_text(uploaded_file)

            document_id = save_document(
                uploaded_file.name,
                file_path,
                pdf_text
            )

            # Keep the latest uploaded document active
            st.session_state.pdf_content = pdf_text
            st.session_state.uploaded_file_name = uploaded_file.name
            st.session_state.selected_document_id = document_id

            progress.progress((index + 1) / total_files)

            st.success(f"✅ {uploaded_file.name} uploaded successfully.")

    # Refresh document list
    st.session_state.documents = get_all_documents()

st.divider()


# ---------------------------------
# Current Active Document
# ---------------------------------
st.subheader("📄 Current Active Document")

if st.session_state.uploaded_file_name:

    col1, col2 = st.columns(2)

    with col1:
        st.success(
            f"**Document:** {st.session_state.uploaded_file_name}"
        )

    with col2:
        st.info(
            f"**Characters:** {len(st.session_state.pdf_content):,}"
        )

else:

    st.warning("No document selected.")


# ---------------------------------
# Uploaded Documents
# ---------------------------------
st.divider()

st.subheader("📚 Uploaded Documents")

documents = get_all_documents()

if documents:

    for document in documents:

        st.write(
            f"📄 {document['file_name']}"
        )

else:

    st.info("No documents uploaded yet.")


st.divider()

st.caption(
    "💡 Upload one or more PDFs. Document selection will be available from the Chat page."
)