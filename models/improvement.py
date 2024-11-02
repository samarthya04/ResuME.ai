from models.ats_scoring import extract_keywords

def suggest_improvements(resume_text, jd_keywords):
    resume_keywords = set(extract_keywords(resume_text))
    missing_keywords = jd_keywords - resume_keywords
    suggestions = {
        "Add Keywords": list(missing_keywords),
        "Use Simple Formatting": "Avoid tables, graphics, and fancy fonts."
    }
    return suggestions
