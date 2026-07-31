import mysql.connector

from config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)


# -----------------------------------
# Database Connection
# -----------------------------------
def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# ==========================================================
# Document Functions
# ==========================================================

# -----------------------------------
# Save Document
# -----------------------------------
def save_document(file_name, file_path, document_text):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO documents
    (
        file_name,
        file_path,
        document_text
    )
    VALUES
    (
        %s,
        %s,
        %s
    )
    """

    cursor.execute(
        query,
        (
            file_name,
            file_path,
            document_text
        )
    )

    conn.commit()

    document_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return document_id


# -----------------------------------
# Get Latest Uploaded Document
# -----------------------------------
def get_latest_document():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        id,
        file_name,
        file_path,
        document_text
    FROM documents
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    document = cursor.fetchone()

    cursor.close()
    conn.close()

    return document


# -----------------------------------
# Get All Documents
# -----------------------------------
def get_all_documents():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        id,
        file_name,
        file_path
    FROM documents
    ORDER BY id DESC
    """

    cursor.execute(query)

    documents = cursor.fetchall()

    cursor.close()
    conn.close()

    return documents


# -----------------------------------
# Get Document By ID
# -----------------------------------
def get_document_by_id(document_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        id,
        file_name,
        file_path,
        document_text
    FROM documents
    WHERE id = %s
    """

    cursor.execute(query, (document_id,))

    document = cursor.fetchone()

    cursor.close()
    conn.close()

    return document


# -----------------------------------
# Delete Document
# -----------------------------------
def delete_document(document_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Delete related chat history first
    cursor.execute(
        """
        DELETE FROM chat_history
        WHERE document_id = %s
        """,
        (document_id,)
    )

    # Delete document
    cursor.execute(
        """
        DELETE FROM documents
        WHERE id = %s
        """,
        (document_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()


# ==========================================================
# Chat Functions
# ==========================================================

# -----------------------------------
# Save Chat
# -----------------------------------
def save_chat(document_id, question, answer):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO chat_history
    (
        document_id,
        user_message,
        ai_response
    )
    VALUES
    (
        %s,
        %s,
        %s
    )
    """

    cursor.execute(
        query,
        (
            document_id,
            question,
            answer
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


# -----------------------------------
# Get Chat History
# -----------------------------------
def get_chat_history(document_id=None):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if document_id is None:

        query = """
        SELECT
            id,
            document_id,
            user_message,
            ai_response,
            created_at
        FROM chat_history
        ORDER BY id DESC
        """

        cursor.execute(query)

    else:

        query = """
        SELECT
            id,
            document_id,
            user_message,
            ai_response,
            created_at
        FROM chat_history
        WHERE document_id = %s
        ORDER BY id DESC
        """

        cursor.execute(query, (document_id,))

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history