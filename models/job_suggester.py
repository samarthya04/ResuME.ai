import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def suggest_jobs(resume_keywords):
    # Load job titles from the CSV
    job_titles_df = pd.read_csv("data/job_titles.csv")
    
    # Debugging: Print the columns and first few rows
    print("Job Titles DataFrame Columns:", job_titles_df.columns)
    print("Job Titles DataFrame Head:\n", job_titles_df.head())

    # Access the correct column for job descriptions
    if 'job description' not in job_titles_df.columns:
        raise KeyError("The 'job description' column is missing from the job_titles DataFrame.")
    
    # Vectorize job descriptions using the correct column name
    vectorizer = TfidfVectorizer()
    job_desc_matrix = vectorizer.fit_transform(job_titles_df['job description'])

    # Continue with your job suggestion logic...
    # For example, you might want to calculate similarities and return suggestions
    # Here, just return the job titles for now
    job_titles = job_titles_df['Job title'].tolist()
    return job_titles  # Replace with actual suggestions based on the resume keywords
