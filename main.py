# %%
from src.classifier.client import classify

if __name__ == "__main__":
    prompt = "Hi, I have a problem with my travel booking."
    result = classify(prompt)
    print(result)
