# Simple Temporal Logic Demo for Activity Recognition
# Checks if event B happens after event A with a time constraint

def check_temporal_rule(event_A_time, event_B_time, max_delay):
    """
    Returns True if event B occurs within max_delay seconds after event A
    """
    return 0 < (event_B_time - event_A_time) <= max_delay

# Example usage (could be sensor data timestamps):
event_A = 100  # timestamp in seconds
event_B = 150
max_allowed_delay = 60

print(f"Events follow temporal rule: {check_temporal_rule(event_A, event_B, max_allowed_delay)}")
