# 🧠 Gyanibaba – AI Personal Knowledge Assistant

> **An AI-powered personal knowledge assistant that allows users to upload PDF documents and ask questions in natural language using Google Gemini.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 🔗 Live Demo

**[Launch Gyanibaba](https://gyanibaba-ai.streamlit.app)**

---

## ✨ Features

- 💬 **AI-Powered Chatbot** — Ask questions in natural language.
- 📄 **PDF Document Upload** — Upload one or multiple PDF documents.
- 🤖 **Context-Aware Answers** — Get answers based on extracted document content.
- 🧠 **Google Gemini Integration** — Generate intelligent responses using the Gemini API.
- 📝 **Chat History Storage** — Store conversations in a MySQL database.
- 🗄️ **Cloud Database Support** — Persist document text and chat records using MySQL/Aiven.
- 📚 **Document Management Foundation** — Retrieve uploaded document records from the database.
- ⚡ **Interactive Web Interface** — Use a simple, intuitive Streamlit application.
- ☁️ **Cloud Deployment** — Access the application online through Streamlit Community Cloud.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web interface |
| Google Gemini API | AI-powered responses |
| MySQL / Aiven | Document and chat data storage |
| PyPDF | PDF text extraction |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and collaboration |
| Streamlit Community Cloud | Application deployment |

---

## 🏗️ Project Architecture

The application follows a straightforward workflow:

1. The user uploads one or more PDF documents.
2. PyPDF extracts text from the uploaded files.
3. The extracted document text and metadata are stored in the MySQL database.
4. The user asks questions about the uploaded content.
5. Google Gemini generates responses using the relevant document context provided by the application.
6. Chat records are stored in MySQL for persistence.

---

## 📂 Project Structure

```text
Gyanibaba/
│
├── app.py                  # Main application and dashboard
├── pages/                  # Streamlit pages
├── utils/
│   ├── database.py          # Database operations
│   ├── pdf_reader.py        # PDF text extraction
│   └── session.py           # Session state management
│
├── uploads/                # Local upload directory, if used
├── assets/                 # Static assets
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables (not committed)
├── .gitignore              # Git exclusion rules
└── README.md               # Project documentation
```

*Note: The structure above represents the main project components. Individual files may vary as development progresses.*

---

## ⚙️ Installation and Setup

### Prerequisites

Before running Gyanibaba locally, ensure you have:

- Python 3.x installed
- Git installed
- A Google Gemini API key
- A MySQL database or Aiven MySQL instance

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Gyanibaba
```

Replace `<repository-url>` with the actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your own credentials:

```env
GOOGLE_API_KEY=your_gemini_api_key
DB_HOST=your_database_host
DB_PORT=3306
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

Replace the example values with your actual credentials. Configure the database port and any required TLS/SSL settings according to your database provider.

**Security reminder:** Never commit your `.env` file, API keys, or database passwords to GitHub.

### 5. Start the Application

```bash
streamlit run app.py
```

The application should open in your browser. If it does not, follow the local URL printed in the terminal.

---

## ☁️ Deployment

Gyanibaba is deployed using **Streamlit Community Cloud**.

To deploy your own instance:

1. Push the project to a GitHub repository.
2. Sign in to Streamlit Community Cloud.
3. Create a new app and select the repository and entry-point file (`app.py`).
4. Add the required API and database credentials through the app's Secrets settings.
5. Deploy the application and verify the database connection.

Keep secrets out of source control. The deployed application must be configured to read its credentials from Streamlit Secrets or another appropriate environment configuration mechanism.

---

## 🔮 Future Roadmap

The following improvements are planned to expand Gyanibaba into a more capable personal knowledge assistant.

- [ ] 🔐 **User Authentication and Authorization** — Secure user accounts and provide private document libraries and chat histories.
- [ ] 📚 **Advanced Knowledge Base Management** — View, search, organize, and delete uploaded documents through a dedicated interface.
- [ ] 💬 **Multi-Document Conversations** — Ask questions across multiple uploaded PDFs in a single conversation.
- [ ] 🧠 **Retrieval-Augmented Generation (RAG)** — Retrieve relevant document chunks to improve answer relevance and support larger documents.
- [ ] 📌 **Source References and Citations** — Display relevant document passages and page references alongside generated answers.
- [ ] 🗃️ **Vector Database Integration** — Enable semantic search using embeddings and a vector database.
- [ ] 🎙️ **Voice Interaction** — Support voice-based questions and spoken AI responses.
- [ ] 📊 **Document Insights and Summaries** — Generate summaries, key takeaways, and topic overviews.
- [ ] ☁️ **Scalable Cloud File Storage** — Store original PDF files using cloud object storage.
- [ ] 🛡️ **Security and Performance Improvements** — Strengthen input validation, error handling, API usage controls, and document processing.
- [ ] 📱 **Responsive User Experience** — Improve usability across desktop, tablet, and mobile devices.

*Roadmap items are planned enhancements and may change as development progresses.*

---

## 👨‍💻 Team

**Project:** Gyanibaba – AI Personal Knowledge Assistant

**Team Members:**

1. **Md Zabed Aktar Khan** — [GitHub](https://github.com/Zabed05/)
2. **Kumaresh Jana** — [GitHub](https://github.com/iamkumaresh/)
3. **Akash Khan** — [GitHub](https://github.com/akash-on-web/)
4. **Hritwik Mondal** — [GitHub](https://github.com/HRITWIK11/)
5. **Mojammel Hossain Sha** — [GitHub](https://github.com/mojammel386/)

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Commit your changes with a descriptive message.
5. Open a pull request describing your improvements.

---

## 🔒 Security

- Store API keys and database credentials in environment variables or deployment secrets.
- Never upload secrets or private configuration files to GitHub.
- Validate uploaded documents before processing.
- Avoid exposing sensitive document content or credentials in application logs.

If you discover a security issue, please report it responsibly to the project maintainers.

---

## ⭐ Support the Project

If you find **Gyanibaba** useful, consider giving the repository a ⭐ **Star** on GitHub.

Your support helps the project grow and encourages future improvements.

---

<p align="center">
  Made with ❤️ using Python, Streamlit, Google Gemini, and MySQL.
</p>
