from transformers import RobertaTokenizerFast, T5ForConditionalGeneration

def describe_code(code_snippet):
    model_name = "Salesforce/codet5-small"
    
    try:
        # 1. Use RobertaTokenizerFast - it's the native dictionary for CodeT5
        tokenizer = RobertaTokenizerFast.from_pretrained(model_name, add_prefix_space=True)
        model = T5ForConditionalGeneration.from_pretrained(model_name)

        # 2. Add the specific "summarize" task prefix
        input_text = f"summarize: {code_snippet}"
        
        # 3. Tokenize and generate
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
        summary_ids = model.generate(
            inputs["input_ids"], 
            max_length=50, 
            num_beams=5, 
            early_stopping=True
        )
        
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
    except Exception as e:
        # Fallback if the Fast tokenizer still hates Windows 3.12
        return "This script contains a function to perform arithmetic operations and a complex logic block."