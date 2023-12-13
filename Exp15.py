MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char != ' ':
            morse_code += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            morse_code += ' '
    return morse_code


def morse_to_text(morse_code):
    morse_code += ' '
    text = ''
    morse_char = ''
    for char in morse_code:
        if char != ' ':
            morse_char += char
        else:
            if morse_char != '':
                text += list(MORSE_CODE_DICT.keys()
                             )[list(MORSE_CODE_DICT.values()).index(morse_char)]
                morse_char = ''
            else:
                text += ' '
    return text


def main():
    print("Choose an option:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text = input("Enter the text to convert to Morse code: ")
        morse_result = text_to_morse(text)
        print(f"Morse code: {morse_result}")
    elif choice == '2':
        morse_code = input("Enter the Morse code to convert to text: ")
        text_result = morse_to_text(morse_code)
        print(f"Text: {text_result}")
    else:
        print("Invalid choice. Please enter either '1' or '2'.")


if __name__ == "_main_":
    main()
