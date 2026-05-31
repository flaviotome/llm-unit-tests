from src.classifier.client import classify
from src.classifier.schemas import Category


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def get_llm_result(prompt: str):
    """
    Call the LLM and return a validated ClassifierResult object.

    Fields accessible on the result:
        result.category      → Category.BOOKING | Category.PAYMENT | Category.STAY
        result.confidence    → Confidence.HIGH  | Confidence.MEDIUM | Confidence.LOW
        result.justification → str
    """
    # Step 1 – call the real LLM; classify() handles JSON parsing and validation
    return classify(prompt)


# ---------------------------------------------------------------------------
# Tests — one per category defined in CONFIG_PROMPT
# ---------------------------------------------------------------------------

def test_category_booking():
    """A message about booking problems should be classified as BOOKING."""

    # Step 1 – choose a prompt that clearly describes a booking issue
    prompt = "I need to cancel my reservation for next weekend."

    # Step 2 – call the LLM and get the validated result
    result = get_llm_result(prompt)

    # Step 3 – assert the expected category using the enum (no raw strings)
    assert result.category == Category.BOOKING, (
        f"Expected BOOKING but got '{result.category}'. Full response: {result}"
    )


def test_category_payment():
    """A message about payment problems should be classified as PAYMENT."""

    # Step 1 – choose a prompt that clearly describes a payment issue
    prompt = "I was charged twice on my credit card for the same booking."

    # Step 2 – call the LLM and get the validated result
    result = get_llm_result(prompt)

    # Step 3 – assert the expected category using the enum
    assert result.category == Category.PAYMENT, (
        f"Expected PAYMENT but got '{result.category}'. Full response: {result}"
    )


def test_category_stay():
    """A message about stay quality should be classified as STAY."""

    # Step 1 – choose a prompt that clearly describes a stay/accommodation issue
    prompt = "The room I received was dirty and the air conditioning was not working."

    # Step 2 – call the LLM and get the validated result
    result = get_llm_result(prompt)

    # Step 3 – assert the expected category using the enum
    assert result.category == Category.STAY, (
        f"Expected STAY but got '{result.category}'. Full response: {result}"
    )
