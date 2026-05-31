import os
import json

from google import genai
from google.genai import types
from dotenv import load_dotenv

from .prompts import CONFIG_PROMPT
from .schemas import ClassifierResult

load_dotenv()

_API_KEY = os.environ.get("GEMINI_API_KEY")
_MODEL   = "gemini-2.5-flash"


def call_gemini_api(prompt: str) -> str:
    """
    Send a prompt to the Gemini API and return the raw response text.
    All streamed chunks are collected and printed as they arrive.
    """
    client = genai.Client(api_key=_API_KEY)

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    config = types.GenerateContentConfig(
        system_instruction=CONFIG_PROMPT,
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
    )

    # Collect all streamed chunks into a single string and return it
    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=_MODEL,
        contents=contents,
        config=config,
    ):
        if text := chunk.text:
            print(text, end="", flush=True)
            response_text += text

    print()  # newline after streaming finishes
    return response_text


def classify(prompt: str) -> ClassifierResult:
    """
    Send a prompt to the Gemini API and return a validated ClassifierResult.
    Strips markdown code fences the model may add around the JSON.
    """
    raw = call_gemini_api(prompt)

    # Strip optional ```json ... ``` fences
    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    return ClassifierResult.model_validate(json.loads(clean))
