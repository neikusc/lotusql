import sys, pathlib
PROJECT_ROOT = pathlib.Path('/Users/kientrinh/src/agents/lotusql').resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.models.lite_llm import LiteLlm
from src.lotusql.interact_with_agent import call_agent_async
from src.lotusql.data_retrieval import data_retrieval, TABLE_SCHEMA
from src.lotusql.tools import get_today_weather, get_current_datetime
from src.lotusql.initialize_service import MODEL_NAME
import asyncio

# from src.lotusql.initialize_service import MODEL_NAME

agent = Agent(
    name = "data_agent",
    model=LiteLlm(MODEL_NAME, stream=True),
    description = f"Analyze user's query and write a SQL query before executing it on database to retrieve information. Here is the schema of the table you got access: {TABLE_SCHEMA}.",
    instruction = "You are a data admin.",
    tools=[data_retrieval,
           get_today_weather, 
           get_current_datetime]
)

APP_NAME = ""
USER_ID = "user_1"
SESSION_ID = 'session_001'

async def initialize_runner():
    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name = APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(
        agent = agent,
        app_name = APP_NAME,
        session_service=session_service
    )
    return runner

runner = asyncio.run(initialize_runner())

async def run_conversation(user_query):
    response = await call_agent_async(query = user_query,
                                      runner=runner,
                                      user_id=USER_ID,
                                      session_id=SESSION_ID)
    return response

if __name__ == "__main__":
    # prompt = "What is the weather today in San Diego?"
    # prompt = "What is the total number of records?"
    # prompt = "How many properties have 3+ bedrooms and 2+ bathrooms?"
    # prompt = "How many properties were built after 2000?"
    # prompt = "Can you give me the breakdown of properties by neighborhood? how many properties are there in each neighborhood?"
    # prompt = "Find top 5 most crowded neighborhoods with the highest number of properties."
    prompt = "Find top 5 most expensive neighborhoods and their average prices."
    # prompt = "What time is it?"
    response = asyncio.run(run_conversation(user_query=prompt))
    print(response)