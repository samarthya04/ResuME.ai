from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text):
    vectorizer = CountVectorizer(max_features=20, stop_words="english")
    keywords = vectorizer.fit_transform([text]).toarray()
    return vectorizer.get_feature_names_out()

def calculate_ats_score(resume_text, jd_keywords):
    resume_keywords = extract_keywords(resume_text)
    score = len(set(resume_keywords) & jd_keywords) / len(jd_keywords) * 100
    return round(score, 2)
