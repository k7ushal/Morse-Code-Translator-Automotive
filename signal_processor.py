# Project: Automotive Signal Encoding & Decoding System
# Description: Pulse-based diagnostic communication simulator (A-Z, 0-9)
# Author: Kaushal

# Pulse Signal Mapping
SIGNAL_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '---..', '8': '---..', '9': '----.', 
    '0': '-----', ' ': '/'
}

def encode_data(message):
    """Encodes string data into pulse-width signals."""
    encoded_output = []
    for char in message.upper():
        if char in SIGNAL_MAP:
            encoded_output.append(SIGNAL_MAP[char])
        else:
            encoded_output.append('?') # Error handling for unknown characters
    return ' '.join(encoded_output)

def decode_data(signal):
    """Decodes pulse-width signals back into string data."""
    reverse_map = {v: k for k, v in SIGNAL_MAP.items()}
    signals = signal.split(' ')
    decoded_output = []
    for s in signals:
        if s in reverse_map:
            decoded_output.append(reverse_map[s])
        else:
            decoded_output.append('?')
    return ''.join(decoded_output)

def run_system():
    print("--- AUTOMOTIVE SIGNAL PROCESSOR v1.0 ---")
    
    while True:
        print("\n[1] ENCODE DATA\n[2] DECODE DATA\n[3] SYSTEM EXIT")
        operation = input("Select Operation: ")
        
        if operation == '1':
            data = input("Enter Message: ")
            print(f"Signal Output: {encode_data(data)}")
        elif operation == '2':
            data = input("Enter Signal Input: ")
            print(f"Data Output: {decode_data(data)}")
        elif operation == '3':
            print("System Shutdown.")
            break
        else:
            print("Operation Error: Invalid Input.")

if __name__ == "__main__":
    run_system()
          
