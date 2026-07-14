import requests


class OllamaClient:

    def __init__(
        self,
        model="llama3.2:3b",
        url="http://localhost:11434/api/generate"
    ):
        self.model = model
        self.url = url

    def ask(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "").strip()

        except Exception as e:
            return f"Error: {e}"