import requests

def get_quote(mood):
    try:
        response = requests.get("https://zenquotes.io/api/random", verify=True)
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            return data[0].get("q", "No quote available.")
        else:
            return "No quote available."
    
    except Exception as e:
        print("Error fetching quote:", e)
        return "Error fetching quote."
