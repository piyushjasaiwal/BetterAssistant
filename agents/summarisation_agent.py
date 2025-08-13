# content -> summarisation pipeline and return the results
from transformers import pipeline

class Summariser:
    def __init__(self, model="facebook/bart-large-cnn"):
        self.model = model
        self.summariser_pipeline = pipeline("summarization", model=model)

    def summarise(self, content: str) -> str:
        summary = self.summariser_pipeline(content, max_length=100, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    

# summariser = Summariser()
# text="""
# In a crooked alley tucked behind the spice bazaar, there lived a clockmaker named Elian who never sold a single clock. His shop was filled with timepieces—grandfather clocks, pocket watches, cuckoos—all ticking in perfect harmony, yet none bore a price tag.
# Locals whispered that Elians clocks did not measure time—they bent it.
# One rainy evening, a girl named Mira wandered in, soaked and curious. “Why do not you sell them” she asked.
# Elian smiled, eyes twinkling. “Because time is not for sale. But it can be borrowed.”
# He handed her a small brass watch. “Think of a moment you wish to relive.”
# Mira closed her eyes and thought of her mothers laugh, lost to memory. The watch ticked once—then silence.
# When she opened her eyes, she was five again, sitting on her mothers lap, wrapped in warmth and lullabies.
# The moment lasted only a breath, but Mira wept with gratitude.
# Elian took back the watch. “One moment per soul” he said gently.
# Years passed. Mira became a historian, obsessed with time. But she never forgot the alley, the clocks, or the man who whispered to time itself.
# And every year, on the rainiest day, she left a flower at his door

# """
# print(summariser.summarise(text))
    