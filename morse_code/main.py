import machine
from time import sleep

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
MORSE_CODE_TIMES = {'.': 1, '-': 2}

morse_pin = machine.Pin(16, machine.Pin.OUT)


def morse_code(phrase, pin):
    for word in phrase.split():  # splits our phrase into words
        for letter in word:
            code = MORSE_CODE_DICT.get(letter.upper())
            for symbol in code:
                pin.value(0)
                sleep(MORSE_CODE_TIMES.get(symbol))
                pin.value(1)
                sleep(1) # Sleep for 1 second between dots and dashes
            sleep(2)  # Sleep for 3 seconds between letters (includes 1 second from end of dot and dash)
        sleep(4)  # Sleep for 7 seconds between words (includes 3 seconds from end of letter)
    return True

sleep(1)
morse_code('Hello World', morse_pin)

