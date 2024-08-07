from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = """
The Olympic Games, held every four years, are a global event showcasing the pinnacle of athletic achievement. Athletes from around the world gather to compete in a wide range of sports, from swimming and gymnastics to track and field and team events like basketball and soccer. The Olympics are not only a display of physical prowess but also a celebration of international unity and cultural exchange. The event has a rich history, dating back to ancient Greece, and has evolved to include both summer and winter games, each with its own unique set of challenges and competitions. Hosting the Olympics is considered a prestigious honor, bringing significant attention and tourism to the host city, while also promoting the Olympic values of excellence, friendship, and respect.
"""
summary = summarize_text(text)
print(summary)
