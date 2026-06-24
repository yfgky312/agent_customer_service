from typing import Dict, Any, List
from datetime import datetime

class AgentState:
    def __init__(self):
        self.messages: List[Dict[str, str]] = []  # 对话历史
        self.current_ticket: Dict[str, Any] = {}   # 当前工单
        self.retrieved_docs: List[str] = []        # 检索到的文档
        self.draft: str = ""                       # 回复草稿
        self.review_result: Dict[str, Any] = {}    # 审核结果
        self.final_response: str = ""              # 最终回复

state = AgentState()