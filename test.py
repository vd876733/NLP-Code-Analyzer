import math

class DataProcessor:
    def __init__(self, data):
        self.d = data # Smell: Single letter variable

    def calculate_recursive_factorial(self, n):
        # Smell: Short variable name 'n'
        if n == 0:
            return 1
        else:
            return n * self.calculate_recursive_factorial(n-1)

    def process_and_analyze_complex_dataset_with_logic(self, val, multiplier):
        # Smell: Long Method (Intentionally stretched logic)
        a = val
        b = multiplier
        
        # Complex calculation block
        res = (a * b) + math.sqrt(a)
        final_list = []
        
        # Unnecessarily long loop to trigger the 'Long Method' smell
        for i in range(10):
            x = res * (i + 1)
            y = x / 2
            z = y + self.calculate_recursive_factorial(5)
            
            if z > 100:
                final_list.append(z)
            
            # Deeply nested logic
            if len(final_list) > 2:
                for item in final_list:
                    p = item * 0.1
                    q = p + math.sin(p)
                    print(f"Computed trace: {q}")
        
        return final_list

# Execution
data_obj = DataProcessor([1, 2, 3])
output = data_obj.process_and_analyze_complex_dataset_with_logic(10, 5)
print("Analysis Complete:", output)