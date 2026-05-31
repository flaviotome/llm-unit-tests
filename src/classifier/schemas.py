from enum import Enum
from pydantic import BaseModel


class Category(str, Enum):
    BOOKING = "BOOKING"
    PAYMENT = "PAYMENT"
    STAY    = "STAY"


class Confidence(str, Enum):
    HIGH   = "HIGH"
    MEDIUM = "MEDIUM"
    LOW    = "LOW"


class ClassifierResult(BaseModel):
    """Typed representation of the JSON the LLM always returns."""
    category:      Category
    confidence:    Confidence
    justification: str
