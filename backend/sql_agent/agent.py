
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains.sql_database.query import create_sql_query_chain

from backend.db import engine
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

db = SQLDatabase(engine)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    google_api_key=api_key,
    temperature=0
)

chain = create_sql_query_chain(llm, db)

def generate_sql(question: str):

    raw_sql = chain.invoke({"question": question})

    raw_sql = raw_sql.replace("```sql", "").replace("```", "").strip()

    if "SQLQuery:" in raw_sql:
        raw_sql = raw_sql.split("SQLQuery:")[1].strip()

    if not raw_sql.lower().startswith("select"):
        raise ValueError("Only SELECT queries allowed")

    print(raw_sql)

    return raw_sql