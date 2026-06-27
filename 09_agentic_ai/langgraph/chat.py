from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="oc/deepseek-v4-flash-free", 
    openai_api_key="sk-719d884a18031265-clqr0i-fc76061e", 
    openai_api_base="http://localhost:20128/v1" 
)
response = llm.invoke("Hello, how are you?")
print(response.content)



