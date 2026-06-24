from agents.base import BaseAgent
from state import state


class DraftAgent(BaseAgent):
    def __init__(self):
        super().__init__("Draft")

    def run(self, context: dict) -> dict:
        user_input = state.current_ticket.get("user_input", "")
        retrieved = state.retrieved_docs[0] if state.retrieved_docs else ""
        self._log("正在生成回复草稿...")

        prompt = f"""
你是客服人员，请根据以下信息生成回复草稿：

用户问题: {user_input}

检索到的答案:
{retrieved}

要求：
1. 语气专业、友好
2. 直接回答用户问题
3. 如果信息不足，请说明需要进一步确认

输出格式：
草稿: xxx
"""

        result = self._call_llm(prompt)
        self._log(f"草稿生成完成，长度: {len(result)} 字符")

        state.draft = result
        return {"draft": result, "status": "drafted"}