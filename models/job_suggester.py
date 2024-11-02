import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def suggest_jobs(resume_keywords):
    job_titles_df = pd.read_csv("data/job_titles.csv")
    
    print("Job Titles DataFrame Columns:", job_titles_df.columns)
    print("Job Titles DataFrame Head:\n", job_titles_df.head())

    vectorizer = TfidfVectorizer()
    job_desc_matrix = vectorizer.fit_transform(job_titles_df['job description'])

    job_titles = job_titles_df['Job title'].tolist()
    return job_titles  
