# 🧠 AI Job Matching System - TK Company

A professional web-based system that allows HR recruiters to upload candidate resumes in PDF or TXT format, compare them to a job description using AI (BERT embeddings), and retrieve a ranked list of the best matches.

---
<img src="https://github.com/user-attachments/assets/238427f4-e49b-49fd-9ab1-ad0f2355b14f" width="400" hight ="400"></br>
<img src="https://github.com/user-attachments/assets/e584ea1c-f998-457a-b16d-c136ed9b72bb" width="400" hight ="400">

## 🚀 Project Overview

This system helps companies streamline the recruitment process using **state-of-the-art NLP models**. Instead of manually reading resumes, the recruiter simply:

1. Enters a job description.
2. Uploads multiple resumes.
3. Gets a sorted list of the most relevant candidates, with **download links** and **match scores**.

---


## 🎯 Features

- ✅ Upload multiple `.pdf` and `.txt` resumes.
- ✅ BERT-based intelligent matching using [`sentence-transformers`](https://www.sbert.net/).
- ✅ Clean and responsive UI with dark theme.
- ✅ Download CVs directly from the result table.
- ✅ Top match highlighted with light green for visual clarity.

---

## 🛠️ Tech Stack

| Component        | Tech Used                              |
|------------------|------------------------------------------|
| Backend          | Python, Flask                           |
| NLP Model        | `all-MiniLM-L6-v2` (from SentenceTransformers) |
| PDF Extraction   | PyMuPDF (`fitz`)                        |
| Frontend UI      | HTML, CSS (custom gradient design)      |

---

## 📂 Project Structure

aiforcv/
├── app.py                   # Main application file
├── requirements.txt         # Project dependencies
├── UpdatedResumeDataSet.csv 
│
├── uploads/                 # Folder for uploaded resumes
│
└── templates/               # Flask HTML templates
    └── index.html           # Main UI for the app
    



 
