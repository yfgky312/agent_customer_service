# 企业智能客服 Multi-Agent 系统

基于 LangGraph 的多 Agent 协作系统，模拟真实企业客服场景，自动完成工单分类、知识库检索、回复草稿生成和质量审核。

```plaintext
## 系统架构

用户输入
↓
ClassifierAgent（意图分类 + 优先级评估）
↓
RetrievalAgent（知识库检索）
↓
DraftAgent（生成回复草稿）
↓
ReviewAgent（合规审核）
↓
输出最终回复


## 核心 Agent

| Agent | 职责 |
|-------|------|
| **ClassifierAgent** | 对用户输入进行意图分类（技术/产品/账单/通用），评估优先级 |
| **RetrievalAgent** | 从知识库（FAQ）中检索与用户问题最相关的答案 |
| **DraftAgent** | 基于检索结果生成回复草稿 |
| **ReviewAgent** | 审核草稿质量，做合规校验，决定是否通过或转人工 |

## 技术栈

- Python 3.12
- LangChain + LangGraph
- DeepSeek 8B (本地部署)
- FastAPI（可扩展）

## 快速开始

```bash
# 1. 进入项目目录
cd agent_customer_service

# 2. 运行
python main.py

## 演示效果

运行后，系统会自动处理一条测试工单，完整展示从分类到审核的全流程：

```plaintext
用户输入：我遇到一个bug，系统登录后页面一直加载不出来

[Classifier] 意图：technical，优先级：高
[Retrieval] 检索完成
[Draft] 草稿生成完成
[Review] 审核通过
→ 最终回复：xxx

可扩展方向

· 接入真实知识库（PDF/Word/数据库）
· 增加会话记忆（Redis）
· 开发 Web 界面（Streamlit/FastAPI）
· 接入真实工单系统

项目价值

· 模拟真实企业客服场景
· 完整展示 Multi-Agent 协作流程
· 可演示、可讲解、可扩展
