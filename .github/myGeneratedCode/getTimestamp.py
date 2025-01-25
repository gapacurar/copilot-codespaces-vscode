from datetime import datetime

def create_timestamp():
    # Get the current date and time
    now = datetime.now()
    
    # Format the timestamp
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return timestamp

# Example usage:
if __name__ == "__main__":
    print("Current Timestamp:", create_timestamp())