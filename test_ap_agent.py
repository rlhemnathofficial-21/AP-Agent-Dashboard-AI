from data.load_data import load_invoice_master
from agents.ap_ai_agent import APAIAgent

# Load AP dataset
df = load_invoice_master()

# Create AI Agent
agent = APAIAgent()

# Ask a business question
question = "Which vendor has the highest invoice amount?"

answer = agent.ask(df, question)

print("\n===== AI RESPONSE =====\n")
print(answer)