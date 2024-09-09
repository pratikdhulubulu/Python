def find_key_by_value_list(dictionary, target_values):
    for key in dictionary.items():
        # if set(target_values) >= set(values):
        if    
            return key
    return None

# Example dictionary
my_dict = {
    "Key1": [1000, 2000, 3000],
    "Key2": [4000, 5000, 6000],
    "Key3": [7000, 8000, 9000]
}

target_values = [4950, 5090, 6000]
result_key = find_key_by_value_list(my_dict, target_values)

if result_key:
    print(f"Found key: {result_key}")
else:
    print("Key not found for the provided values.")
