from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = """
Our digital assessment system prototype addresses critical gaps in user awareness and knowledge identified during interviews. Many users are unaware of their responsibilities in the SAP GRC PC system, feel underprepared and lack confidence due to insufficient training, and do not know that the system captures issues based on controls that can be accessed through their SAP GRC work inbox. Additionally, training sessions were found to be too high-level and lacking specific examples.
"""
summary = summarize_text(text)
print(summary)
