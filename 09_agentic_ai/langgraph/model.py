from langchain_groq import ChatGroq
from langchain_core import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


llm = ChatGroq(model="gpt-4o", temperature=0.9)



