from agents.classifier import ClassifierAgent
from agents.retrieval import RetrievalAgent
from agents.draft import DraftAgent
from agents.review import ReviewAgent
from state import state


def run_customer_service(user_input: str):
    print("=" * 60)
    print("企业智能客服 Multi-Agent 系统")
    print("=" * 60)
    print(f"用户: {user_input}\n")

    # 1. Classifier
    classifier = ClassifierAgent()
    classifier.run({"user_input": user_input})
    print("\n")

    # 2. Retrieval
    retrieval = RetrievalAgent()
    retrieval.run({})
    print("\n")

    # 3. Draft
    draft = DraftAgent()
    draft.run({})
    print("\n")

    # 4. Review
    review = ReviewAgent()
    result = review.run({})

    print("\n" + "=" * 60)
    print("最终回复")
    print("=" * 60)
    print(state.final_response)

    if not result["passed"]:
        print(f"\n审核结果: {result['review'][:200]}...")
        print("\n→ 此回复需要人工复核")

    print("=" * 60)


if __name__ == "__main__":
    # 测试
    test_input = "我遇到一个bug，系统登录后页面一直加载不出来"
    run_customer_service(test_input)