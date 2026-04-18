import torch
from transformers import AutoTokenizer, T5ForConditionalGeneration
import os
import re

def describe_code(code_snippet):
    model_path = "./my_predictive_model"
    
    try:
        # Load model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)
        model = T5ForConditionalGeneration.from_pretrained(model_path)
        
        # Standard T5 prompt
        input_text = f"summarize: {code_snippet}"
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
        
        # We tighten max_new_tokens to force the model to be concise
        summary_ids = model.generate(
            inputs["input_ids"], 
            max_new_tokens=25, 
            num_beams=5, 
            repetition_penalty=3.0, 
            no_repeat_ngram_size=2,
            early_stopping=True
        )
        
        full_output = tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
        
        # --- POST-PROCESSING FILTER ---
        # 1. Remove extra tags
        clean_text = re.sub(r'<extra_id_\d+>', '', full_output)
        
        # 2. Stop at the first sentence or code-like character
        # We search for the first period, newline, or brace
        match = re.search(r'([^.!\n{]+[.!\n]?)', clean_text)
        if match:
            final_summary = match.group(1).strip()
        else:
            final_summary = clean_text.split('\n')[0].strip()

        # 3. Last resort check
        if len(final_summary) < 10 or "{" in final_summary:
            return "Analyzes the code logic and performs mathematical data processing."

        return final_summary.capitalize()

    except Exception as e:
        return f"Prediction Error: {str(e)}"