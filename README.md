# HelloAgent

一个集成多种 AI Agent 框架的演示项目，展示如何使用不同的智能体技术构建各类 AI 应用。

## 🚀 项目简介

本项目整合了目前最流行的 AI Agent 框架，包括：

- **CAMEL-AI**: 第一个 LLM 多智能体框架
- **Claude Agent SDK**: Anthropic 官方智能体 SDK（支持 Python 和 TypeScript）  
- **LangChain Deep Agent**: 基于 LangChain 的深度智能体
- **LangGraph**: 图结构的智能体工作流框架

## 📦 功能特性

### 🐪 CAMEL-AI 演示
- 多智能体协作框架
- 内置 DuckDuckGo 搜索工具
- 支持自定义智能体角色和任务

### 🤖 Claude Agent SDK
- **Python 版本**: 异步代码审查和自动修复
- **TypeScript 版本**: 同样的功能，不同的语言实现
- 支持文件读取、编辑、搜索等工具
- 可配置权限模式

### 🔍 LangChain Deep Agent
- 专业的研究智能体
- 集成 Tavily 互联网搜索
- 支持不同主题的搜索（通用、新闻、金融）

### 🕸️ LangGraph 聊天机器人
- 基于状态图的对话系统
- 支持流式输出
- 简单易用的交互式聊天界面

## 🛠️ 安装配置

### 环境要求
- Python >= 3.12
- Node.js (用于 TypeScript 演示)

### 1. 克隆项目
```bash
git clone <repository-url>
cd HelloAgent
```

### 2. 安装 Python 依赖
```bash
# 使用 uv（推荐）
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### 3. 安装 Node.js 依赖
```bash
npm install
```

### 4. 环境变量配置

创建 `.env` 文件并配置以下 API 密钥：

```env
# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=your_openai_api_base_url  # 可选，用于代理

# Tavily 搜索 API
TAVILY_API_KEY=your_tavily_api_key

# Claude API（可选）
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## 🎯 使用方法

### CAMEL-AI 演示
```bash
python camel_ai/demo.py
```
展示多智能体协作，自动搜索和回答关于 CAMEL-AI 框架的问题。

### Claude Agent SDK

**Python 版本：**
```bash
python claude_agent_sdk/agent_demo.py
```

**TypeScript 版本：**
```bash
node claude_agent_sdk/agent_demo.ts
```

这两个演示都会：
- 自动审查 `utils.py` 文件
- 检测可能导致崩溃的 bug
- 自动修复发现的问题

### LangChain Deep Agent
```bash
python langchain_deep_agent/search_agent.py
```
运行专业的研究智能体，对指定主题进行深度调研。

### LangGraph 聊天机器人
```bash
python langgraph/01_simple_chatbot.py
```
启动交互式聊天机器人，支持实时对话。

## 📁 项目结构

```
HelloAgent/
├── camel_ai/
│   └── demo.py                 # CAMEL-AI 多智能体演示
├── claude_agent_sdk/
│   ├── agent_demo.py          # Claude SDK Python 演示
│   ├── agent_demo.ts          # Claude SDK TypeScript 演示
│   └── utils.py               # 用于演示的工具函数
├── langchain_deep_agent/
│   └── search_agent.py        # LangChain 搜索智能体
├── langgraph/
│   └── 01_simple_chatbot.py   # LangGraph 聊天机器人
├── main.py                    # 项目入口文件
├── pyproject.toml             # Python 项目配置
├── package.json               # Node.js 依赖配置
└── README.md                  # 项目说明文档
```

## 🔧 主要依赖

### Python 依赖
- `claude-agent-sdk`: Anthropic 官方智能体 SDK
- `deepagents`: 深度智能体框架
- `langchain`: LangChain 核心库
- `langchain-openai`: OpenAI 集成
- `langgraph`: 图结构工作流
- `tavily-python`: Tavily 搜索 API 客户端
- `python-dotenv`: 环境变量管理

### Node.js 依赖
- `@anthropic-ai/claude-agent-sdk`: Claude Agent SDK TypeScript 版本

## 💡 使用技巧

1. **API 密钥管理**: 确保在 `.env` 文件中正确配置所需的 API 密钥
2. **搜索功能**: Tavily 搜索支持不同主题，可根据需要调整搜索参数
3. **权限控制**: Claude Agent SDK 支持不同的权限模式，可根据需要配置
4. **流式输出**: LangGraph 支持流式对话，提供更好的用户体验

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进项目！

## 📄 许可证

本项目遵循 MIT 许可证。

## 🆘 常见问题

### Q: 如何获取所需的 API 密钥？
A: 
- **OpenAI API**: 访问 [OpenAI 平台](https://platform.openai.com/)
- **Tavily API**: 访问 [Tavily 官网](https://tavily.com/)
- **Anthropic API**: 访问 [Anthropic Console](https://console.anthropic.com/)

### Q: 遇到依赖安装问题怎么办？
A: 推荐使用 `uv` 包管理器，它能更好地处理依赖冲突和版本管理。

### Q: 如何自定义智能体的行为？
A: 每个框架都提供了丰富的配置选项，可以通过修改系统提示词、工具集合、模型参数等来定制智能体行为。

---

如有问题或建议，请随时联系项目维护者！