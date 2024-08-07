from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = """
The item is defective (there is a dent). The defect was noticed during inspection.
Further analysis shows that the dent does not affect the functionality. However,
it is recommended to handle such items with care to avoid further damage. 
"""
summary = summarize_text(text)
print(summary)
