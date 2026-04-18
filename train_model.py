import torch
from torch.utils.data import DataLoader, Dataset
from torch.optim import AdamW 
from transformers import AutoTokenizer, T5ForConditionalGeneration
import os

# 1. THE DATASET
data = [
    {"code": "def add(a, b): return a + b", "summary": "Calculates the sum of two numbers."},
    {"code": "import math\ndef get_sqrt(x): return math.sqrt(x)", "summary": "Performs a square root calculation."},
    {"code": "import os\ndef list_files(): return os.listdir()", "summary": "Retrieves a list of files from the directory."},
    {"code": "class DataProcessor: def __init__(self): pass", "summary": "Implements a class for processing data."},
    {"code": "def save_json(data, f): json.dump(data, f)", "summary": "Handles JSON data serialization."},
    {"code": "def factorial(n): return 1 if n==0 else n*factorial(n-1)", "summary": "Calculates the factorial of a number recursively."}
]

class SimpleCodeDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        text = "summarize: " + str(item["code"])
        label = str(item["summary"])

        inputs = self.tokenizer(text, padding="max_length", truncation=True, max_length=128, return_tensors="pt")
        targets = self.tokenizer(label, padding="max_length", truncation=True, max_length=128, return_tensors="pt")
        
        return {
            "input_ids": inputs.input_ids.squeeze(),
            "attention_mask": inputs.attention_mask.squeeze(),
            "labels": targets.input_ids.squeeze()
        }


def load_tokenizer(model_name: str):
    try:
        return AutoTokenizer.from_pretrained(
            model_name,
            use_fast=True,
            legacy=False,
            add_prefix_space=True,
            additional_special_tokens=[],
        )
    except Exception as fast_error:
        print(f"Fast tokenizer failed: {fast_error}")
        print("Falling back to the slow tokenizer.")
        return AutoTokenizer.from_pretrained(
            model_name,
            use_fast=False,
            add_prefix_space=True,
            additional_special_tokens=[],
        )

def main():
    model_name = "Salesforce/codet5-small"
    
    print("--- Phase 1: Loading Model Architecture ---")
    
    tokenizer = load_tokenizer(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    dataset = SimpleCodeDataset(data, tokenizer)
    loader = DataLoader(dataset, batch_size=2, shuffle=True)
    optimizer = AdamW(model.parameters(), lr=5e-5)

    print("--- Phase 2: Starting Training Loop ---")
    model.train()
    for epoch in range(5): 
        total_loss = 0
        for batch in loader:
            optimizer.zero_grad()
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                labels=batch["labels"]
            )
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        print(f"Epoch {epoch+1}/5 | Average Loss: {total_loss / len(loader):.4f}")

    # Save the custom model locally
    output_dir = "./my_predictive_model"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"\n--- Success! Model saved to {output_dir} ---")

if __name__ == "__main__":
    main()