import json
import re
import os
from datasets import load_dataset

def get_last_function_name(code_snippet):
    """
    Finds ALL function names defined in the snippet and returns the LAST one.
    This fixes the issue where helper functions appear before the main solution.
    """
    # Find all strings that look like "def function_name"
    # matches will be a list of strings, e.g., ['is_Power_Of_Two', 'differ_At_One_Bit_Pos']
    matches = re.findall(r"def\s+([a-zA-Z_]\w*)(?=\s*\()", code_snippet)
    
    if matches:
        return matches[-1] # <--- FIX: Return the last one found
    return None

def get_first_function_name(code_snippet):
    """
    For the GENERATED code, we typically want to rename the primary function 
    the model wrote. Usually, the model writes one main function, or puts the 
    main function first.
    """
    match = re.search(r"def\s+([a-zA-Z_]\w*)(?=\s*\()", code_snippet)
    if match:
        return match.group(1)
    return None

def main():
    # File paths
    input_file = "flowgen_mbpp_plus_results.jsonl" 
    output_file = "flowgen_mbpp_plus_corrected_v2.jsonl"

    print("--- 1. Loading EvalPlus/MBPP-Plus Dataset ---")
    dataset = load_dataset("evalplus/mbppplus", split="test")

    # Create a lookup dictionary
    correct_names_map = {}
    
    for item in dataset:
        task_id_formatted = f"Mbpp/{item['task_id']}"
        
        # FIX: Get the LAST function name from the reference code
        # In Mbpp/6, this skips 'is_Power_Of_Two' and grabs 'differ_At_One_Bit_Pos'
        correct_name = get_last_function_name(item['code'])
        
        if correct_name:
            correct_names_map[task_id_formatted] = correct_name

    print(f"Loaded {len(correct_names_map)} reference function names.")

    print(f"--- 2. Processing {input_file} ---")
    
    processed_count = 0
    corrected_count = 0
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip():
                continue
                
            data = json.loads(line)
            task_id = data.get("task_id")
            generated_code = data.get("completion", "")

            if task_id in correct_names_map:
                correct_name = correct_names_map[task_id]
                
                # For the generated code, we grab the name the model chose 
                # (assuming the model wrote a single function block)
                generated_name = get_first_function_name(generated_code)

                if generated_name and generated_name != correct_name:
                    # Debug print for the specific case you caught
                    if task_id == "Mbpp/6":
                        print(f"DEBUG {task_id}: Renaming '{generated_name}' -> '{correct_name}'")
                    
                    pattern = r"def\s+" + re.escape(generated_name) + r"(?=\s*\()"
                    
                    # Replace only the definition
                    data["completion"] = re.sub(pattern, f"def {correct_name}", generated_code, count=1)
                    corrected_count += 1
            
            outfile.write(json.dumps(data) + "\n")
            processed_count += 1

    print("--- Summary ---")
    print(f"Total lines processed: {processed_count}")
    print(f"Functions renamed: {corrected_count}")
    print(f"Corrected file saved to: {output_file}")

if __name__ == "__main__":
    main()