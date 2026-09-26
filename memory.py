import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

print("ENV FILE:", ENV_FILE)
print("ENV EXISTS:", ENV_FILE.exists())
print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint


db = SqliteDb(db_file="agno.db")


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3.8-27b"),
        markdown=True,
        add_history_to_context=True
    )


agent = build_agent()

user_id = "rahul@gmail.com"

agent.print_response(
    "I am Rahul & I am a Data Analyst.",
    user_id=user_id
)

agent.print_response(
    "Who am I?",
    user_id=user_id
)

memories = agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES:")
pprint(memories)