from agents.base import BaseAgent
from state import state


class ClassifierAgent(BaseAgent):
    def __init__(self):
        super().__init__("Classifier")

    def run(self, context: dict) -> dict:
        user_input = context.get("user_input", "")
        self._log(f"正在分类: {user_input[:30]}...")

        prompt = f"""
你是客服工单分类员，请对以下用户输入进行分类：

用户输入: {user_input}

分类标准：
- technical: 技术问题（如bug、部署、代码报错）
- product: 产品功能咨询
- billing: 账单/支付问题
- general: 一般性咨询

输出格式：
意图: xxx
优先级: 高/中/低
"""

        result = self._call_llm(prompt)
        self._log(f"分类结果: {result[:100]}...")

        state.current_ticket = {
            "user_input": user_input,
            "classification": result
        }

        return {"classification": result, "status": "classified"}