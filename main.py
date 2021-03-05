from playsound import playsound
from morse_codes import MORSE_CODE_DICT


def main():
    message = input("Enter your message: ").upper()
    coded_message = encrypt(message)
    return coded_message


def encrypt(message):
    morse_code = ""
    for letter in message:
        if letter != " ":
            playsound(f"audio/{letter}_morse_code.ogg.mp3")
    for letter in message:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += " "
    return morse_code


if __name__ == '__main__':
    print(main())
