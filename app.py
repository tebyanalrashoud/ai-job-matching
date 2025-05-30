import os
import pandas as pd
import fitz  # PyMuPDF for PDFs
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = SentenceTransformer('all-MiniLM-L6-v2')  # BERT-based model

def allowed_file(filename):#check if the extention allowd
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(filepath, ext):#extract the content
    if ext == 'txt':
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    elif ext == 'pdf':
        text = ""
        with fitz.open(filepath) as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    return ""

def match_resumes_to_job(job_description, resumes_data, top_n=10):#compare btween the discription and the cvs and chose the apportate cv
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embeddings = model.encode(resumes_data["Resume"].tolist(), convert_to_tensor=True)
    similarities = util.cos_sim(resume_embeddings, job_embedding)

    resumes_data["MatchingScore"] = [float(score) for score in similarities]
    resumes_data = resumes_data.sort_values(by="MatchingScore", ascending=False).head(top_n)
    return resumes_data

@app.route("/", methods=["GET", "POST"])#run the front (index)
def index():
    results = None
    if request.method == "POST":
        job_description = request.form["job_description"]
        uploaded_files = request.files.getlist("resumes")
        resume_texts = []
        file_links = []

        for file in uploaded_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                ext = filename.rsplit('.', 1)[1].lower()
                text = extract_text(filepath, ext)
                resume_texts.append(text)
                file_links.append(filename)

        if resume_texts:
            df = pd.DataFrame({
                "Resume": resume_texts,
                "Category": ["Uploaded"] * len(resume_texts),
                "Filename": file_links
            })
            results = match_resumes_to_job(job_description, df).to_dict(orient="records")

    return render_template("index.html", results=results)

@app.route("/uploads/<filename>")#if the user uploads files , this func send the right file 
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    print("🔌 Running on: http://127.0.0.1:5000/")
    app.run(debug=True)
