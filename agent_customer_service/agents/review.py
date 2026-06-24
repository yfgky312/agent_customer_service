from agents.base import BaseAgent
from state import state


class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("Review")

    def run(self, context: dict) -> dict:
        draft = state.draft
        self._log(f"正在审核草稿，长度: {len(draft)} 字符")

        prompt = f"""
你是客服质量审核员，请审核以下回复草稿：

草稿内容:
{draft}

审核标准：
1. 是否有敏感词或不当内容？（是/否）
2. 回答是否准确？（是/否）
3. 是否直接回应用户问题？（是/否）
4. 语气是否专业？（是/否）

输出格式：
审核通过: 是/否
原因: xxx
建议: xxx
"""

        result = self._call_llm(prompt)
        self._log(f"审核完成")

        passed = "审核通过: 是" in result
        state.review_result = {"passed": passed, "detail": result}

        if passed:
            state.final_response = draft
        else:
            state.final_response = "⚠️ 此回复需要人工审核，请稍候..."

        return {
            "passed": passed,
            "review": result,
            "final_response": state.final_response,
            "status": "reviewed"
        }