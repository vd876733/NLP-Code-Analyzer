import math
import json

def process_and_analyze_complex_dataset_with_logic(data_input):
    """
    This is a long method designed to trigger the 'Long Method' smell
    while giving the NLP model plenty of tokens to analyze.
    """
    # Ambiguous variables to trigger the 'Ambiguous Name' smell
    a = 10
    b = 20
    x = [i for i in range(a)]
    y = []
    
    # Complex logic loop
    for i in x:
        try:
            # Mathematical operation
            z = math.sqrt(i) * (a / b)
            p = z ** 2
            q = math.factorial(int(z))
            y.append({"id": i, "val": p, "fact": q})
        except Exception as e:
            print(f"Error at index {i}: {e}")
            continue

    # More logic to increase line count
    results = []
    for item in y:
        if item["val"] > 5:
            results.append(item)
        else:
            item["val"] = 0
            results.append(item)

    return results

def main():
    raw_data = "{\"data\": [1, 2, 3, 4, 5]}"
    parsed = json.loads(raw_data)
    final_output = process_and_analyze_complex_dataset_with_logic(parsed)
    print(f"Analysis complete. Found {len(final_output)} items.")

if __name__ == "__main__":
    main()