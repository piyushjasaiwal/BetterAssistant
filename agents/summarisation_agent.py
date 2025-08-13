from transformers import pipeline

class Summariser:
    def __init__(self, model="facebook/bart-large-cnn"):
        self.model = model
        self.summariser_pipeline = pipeline("summarization", model=model)

    def summarise(self, content: str) -> str:
        summary = self.summariser_pipeline(content, max_length=100, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    