from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model="deepseek-r1:8b",
    temperature=0.3,
    timeout=120
)