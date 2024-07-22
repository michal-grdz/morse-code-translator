morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ','
}

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def morse_to_text(morse):
    morse_to_text_dict = {value: key.lower() for key, value in morse_code_dict.items()}
    return ''.join(morse_to_text_dict.get(char, '') for char in morse.split())

if __name__ == "__main__":
    t = "This is a test"
    print(f"Example text: {t}")
    print("In morse code: ", text_to_morse(t))
    m = text_to_morse(t)
    print("Back to latin alphabet: ", morse_to_text(m))    

