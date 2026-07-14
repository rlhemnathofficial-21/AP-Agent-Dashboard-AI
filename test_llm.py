from llm.ollama_client import OllamaClient

llm = OllamaClient()

response = llm.ask(
    "What is Accounts Payable?"
)

print(response)