from agents.base import BaseAgent
from state import state
import os


class RetrievalAgent(BaseAgent):
    def __init__(self):
        super().__init__("Retrieval")

    def run(self, context: dict) -> dict:
        user_input = state.current_ticket.get("user_input", "")
        self._log(f"正在检索: {user_input[:30]}...")

        # 读取知识库
        kb_path = "knowledge_base/faq.txt"
        if os.path.exists(kb_path):
            with open(kb_path, "r", encoding="utf-8") as f:
                faq_content = f.read()
        else:
            faq_content = """
FAQ示例（实际使用时会替换为真实文档）：
Q: 如何重置密码？
A: 点击登录页面的“忘记密码”，按提示操作。

Q: 系统支持哪些支付方式？
A: 支持支付宝、微信支付、银行卡。

Q: 遇到bug怎么反馈？
A: 在工作台点击“反馈”，填写问题描述。
"""

        prompt = f"""
你是知识库检索员，请根据用户问题从FAQ中找出最相关的答案。

用户问题: {user_input}

FAQ内容:
{faq_content}

输出格式：
最相关答案: xxx
相关度: 高/中/低
"""

        result = self._call_llm(prompt)
        self._log(f"检索完成")

        state.retrieved_docs = [result]
        return {"retrieved": result, "status": "retrieved"}