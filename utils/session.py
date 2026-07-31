import streamlit as st


def initialize_session():
    """
    Initialize all Streamlit session state variables.
    """

    # -----------------------------
    # Chat Messages
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------------
    # Current PDF Content
    # -----------------------------
    if "pdf_content" not in st.session_state:
        st.session_state.pdf_content = ""

    # -----------------------------
    # Current Uploaded File Name
    # -----------------------------
    if "uploaded_file_name" not in st.session_state:
        st.session_state.uploaded_file_name = None

    # -----------------------------
    # Selected Document ID
    # -----------------------------
    if "selected_document_id" not in st.session_state:
        st.session_state.selected_document_id = None

    # -----------------------------
    # Uploaded Documents List
    # -----------------------------
    if "documents" not in st.session_state:
        st.session_state.documents = []