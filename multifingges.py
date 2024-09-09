def detect_gesture(flex_values):
    # Define gesture thresholds for each finger and gesture
    thresholds = {
        "Finger1": {
            "Open": [300, 300, 300, 300, 300],
            "Closed": [900, 900, 900, 900, 900]
        },
        "Finger2": {
            "Open": [300, 300, 300, 300, 300],
            "Closed": [900, 900, 900, 900, 900]
        },
        # Define thresholds for other fingers and gestures similarly...
    }
    
    detected_gestures = []
    
    for finger, finger_thresholds in thresholds.items():
        is_open = all(fv < threshold for fv, threshold in zip(flex_values, finger_thresholds["Open"]))
        is_closed = all(fv > threshold for fv, threshold in zip(flex_values, finger_thresholds["Closed"]))
        
        if is_open:
            detected_gestures.append(f"{finger} Open")
        elif is_closed:
            detected_gestures.append(f"{finger} Closed")
    
    if detected_gestures:
        return ", ".join(detected_gestures)
    else:
        return "No Gesture"

# Example flex sensor values for 5 sensors
flex_values = [200, 900, 150, 250, 180]  # Replace with your own sensor values

gesture = detect_gesture(flex_values)
print(f"Detected Gesture(s): {gesture}")
