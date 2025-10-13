from typing import Annotated
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 定义状态类型
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 构建 LangGraph
graph_builder = StateGraph(State)

# 从 .env 中读取配置
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")
model_name = "gpt-4o"

# 设置环境变量（供 LangChain 使用）
os.environ["OPENAI_API_KEY"] = api_key
if api_base:
    os.environ["OPENAI_API_BASE"] = api_base

# 初始化自定义模型
llm = init_chat_model(
    model=model_name,
    model_provider="openai"  # 若是 OpenAI 兼容代理，请保持为 openai
)

# 定义 chatbot 节点
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# 添加节点与边
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

# 流式输出
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

# 主循环
if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except Exception as e:
            print("Error:", e)
            break
