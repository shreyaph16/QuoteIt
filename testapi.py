from src.api import get_quote

mood = "happy"  # Try with different moods like "sad", "motivated"
quote = get_quote(mood)
print("Fetched Quote:", quote)
