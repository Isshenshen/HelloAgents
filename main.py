from hello_agents import SimpleAgent, HelloAgentsLLM
from dotenv import load_dotenv

load_dotenv()

llm = HelloAgentsLLM()

agent = SimpleAgent(
    name = "AI assistant",
    llm = llm,
    system_prompt="you are a useful AI assistant"
)

response = agent.run("hello! please introduce yourself")
print(response)