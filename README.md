# 📄 Chat-with-PDF

A simple AI-powered **Chat with PDF** application built using **Python, Streamlit, LangChain, ChromaDB, Hugging Face Embeddings, and Google Gemini**. Users can upload PDF documents and ask questions based on their content.

---

## 🚀 Features

- 📂 Upload PDF documents
- 📖 Extract text from PDF files
- ✂️ Split documents into chunks
- 🧠 Generate embeddings using Hugging Face
- 💾 Store embeddings in ChromaDB
- 🔍 Retrieve relevant document chunks
- 🤖 Generate answers using Google Gemini
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- Hugging Face Embeddings
- ChromaDB
- PyPDF
- python-dotenv

---

## 📁 Project Structure

```
Chat-with-pdf/
│
├── chatmodels/
│   ├── chat.py
│   └── hugging.py
│
├── embeddingmodels/
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
├── .env
└── uv.lock
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aditya-12-k/Chat-with-pdf.git
```

### 2. Navigate to the project

```bash
cd Chat-with-pdf
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 💡 How It Works

1. Upload a PDF document.
2. The application extracts text from the PDF.
3. The text is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in ChromaDB.
6. The user's question is matched with relevant chunks.
7. Google Gemini generates an answer using the retrieved context.

---

## 📦 Requirements

- Python 3.10+
- Google Gemini API Key
- Internet Connection

---

## 🔮 Future Improvements

- Support multiple PDF uploads
- Chat history
- Source references
- OCR support for scanned PDFs
- Better UI/UX
- Docker support

---


