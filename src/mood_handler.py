import json

def load_theme(mood):
    """Load theme settings based on mood."""
    with open("config/themes.json", "r") as file:
        themes = json.load(file)
    return themes.get(mood, {"bg": "#FFFFFF", "fg": "#000000"})  # Default theme
