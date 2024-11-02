import spacy

nlp = spacy.load("en_core_web_sm")

def parse_job_description(jd_text):
    doc = nlp(jd_text)
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return set(keywords)
