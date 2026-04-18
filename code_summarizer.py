from typing import Any

from transformers import RobertaTokenizer, T5ForConditionalGeneration


def describe_code(code_snippet: str) -> str:
    # Module 5 (Transformers) + Module 6 (Summarization): CodeT5 encoder-decoder generates summaries from code.
    tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-small")
    model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-small")

    inputs = tokenizer(
        "summarize: " + code_snippet,
        return_tensors="pt",
        max_length=512,
        truncation=True,
    )
    output_ids = model.generate(**inputs, max_length=100)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
