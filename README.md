# Hotel Support Classifier

*A hands-on learning project for understanding how to test LLM responses*

A minimal Python project that uses the **Gemini API** to classify hotel support tickets into categories. The goal is to learn and practice the key concepts of testing LLM-powered applications.

## What you will learn

- How to call a real LLM API (Google Gemini) with a system prompt
- How to parse and validate structured JSON responses from an LLM
- How to write integration tests that assert on LLM output
- How to organize a Python AI project following good practices

## Project structure

```
├── src/
│   └── classifier/
│       ├── client.py       # Gemini API call + classify() function
│       ├── prompts.py      # System prompt (CONFIG_PROMPT)
│       └── schemas.py      # Pydantic models for the LLM response
├── tests/
│   └── test_llm.py         # Integration tests — one per category
├── main.py                 # Entry point
├── .env                    # Your API key (never commit this)
├── .env.example            # Template showing required env vars
├── requirements.txt
└── requirements-dev.txt
```

## Prerequisites

- Python 3.11+
- A [Google AI Studio](https://aistudio.google.com/) account with a Gemini API key

## Getting started

**1. Clone and create a virtual environment**

```bash
git clone <repo-url>
cd hotel-support-classifier
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS / Linux
```

**2. Install dependencies**

```bash
pip install -r requirements-dev.txt
```

**3. Configure your API key**

```bash
cp .env.example .env
```

Open `.env` and set your key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the entry point to classify a sample message:

```bash
python main.py
```

The LLM will return a structured JSON response validated by Pydantic:

```json
{
  "category": "BOOKING",
  "confidence": "HIGH",
  "justification": "The user wants to cancel an existing reservation."
}
```

## Running the tests

```bash
pytest tests/ -v
```

Each test sends a real prompt to the Gemini API and asserts on the returned category:

```
tests/test_llm.py::test_category_booking  PASSED
tests/test_llm.py::test_category_payment  PASSED
tests/test_llm.py::test_category_stay     PASSED
```

> [!NOTE]
> These are **integration tests** — they make real API calls and require a valid `GEMINI_API_KEY` in `.env`.

> [!TIP]
> For unit tests you would mock `call_gemini_api()` to avoid API calls and run tests offline. This project intentionally uses real calls to show how to evaluate actual LLM behaviour.

## Key concepts demonstrated

| Concept | Where to look |
|---|---|
| Structuring the system prompt | `src/classifier/prompts.py` |
| Parsing + validating the LLM JSON | `src/classifier/client.py` → `classify()` |
| Typed response model with Pydantic | `src/classifier/schemas.py` |
| Writing assertions on LLM output | `tests/test_llm.py` |
| Keeping secrets out of code | `.env` + `.env.example` |
