from parsers.resume_parser import parse_resume
from parsers.jd_parser import parse_job_description
from models.ats_scoring import calculate_ats_score, extract_keywords
from models.job_suggester import suggest_jobs
from models.improvement import suggest_improvements
import pandas as pd

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def home():
    return render_template("upload.html")  # Serve the upload HTML page

# Analyze route for processing resumes and job descriptions
@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files.get("resume")
    jd_text = request.form.get("job_description")

    if not resume_file or not jd_text:
        return jsonify({"error": "Please provide both a resume file and a job description."}), 400

    # Parse resume and job description
    resume_text = parse_resume(resume_file)
    jd_keywords = parse_job_description(jd_text)

    # Calculate ATS score
    ats_score = calculate_ats_score(resume_text, jd_keywords)

    # Extract resume keywords
    resume_keywords = set(extract_keywords(resume_text))

    # Suggest jobs based on resume keywords
    job_suggestions = suggest_jobs(resume_keywords)

    # Provide improvement suggestions for the resume
    improvements = suggest_improvements(resume_text, jd_keywords)

    return jsonify({
        "ats_score": ats_score,
        "job_suggestions": job_suggestions,
        "improvements": improvements
    })

# Favicon route
@app.route("/favicon.ico")
def favicon():
    return "", 204  # Return a 204 No Content response

if __name__ == "__main__":
    app.run(debug=True)
