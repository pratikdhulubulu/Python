def compare_with_thresholds(input_values, thresholds):
    matched_keys = []
    
    for key, threshold_values in thresholds.items():
        is_within_range = all(abs(iv - tv) <= 30 for iv, tv in zip(input_values, threshold_values))
        if is_within_range:
            matched_keys.append(key)
    
    return matched_keys

# Example input list of 5 values
input_values = [880, 720, 680, 880, 890]

# Example dictionary of threshold values
thresholds = {
    "Gesture1": [700, 900, 900, 900, 900],
    "Gesture2": [900, 700, 900, 900, 900],
    "Gesture3": [900, 710, 710, 900, 900]
}

matched_keys = compare_with_thresholds(input_values, thresholds)

if matched_keys:
    print(f"Matched Keys: {', '.join(matched_keys)}")
else:
    print("No matched keys.")
