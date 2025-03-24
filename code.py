import time  # import the time module and use the sleep( ) function to implement the delay of the lighting stage
from adafruit_circuitplayground import cp  # import the circuit playground control library

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

#get the unit time (0-1 second) entered by the user and ensure that the input is valid
def get_time():
    while True:  # use while loop until the user enters a correct value
        try:
            unit_time = float(input('Enter the length of a unit (0-1s): '))
            if 0 <= unit_time <= 1:  # checks if the input value is between 0 and 1
                return unit_time  # if valid, returns the unit time
            else:
                print('Value must be 0-1. Please try again.')  # if invalid, let the user to re-enter
        except ValueError:
            print('Invalid input. ')  ##if the input is a non-numeric, let the user to re-enter


# convert the sentence to lowercase and remove any character without a Morse code equivalent
def filter_input(text):
    text = text.lower()  # convert the sentence to lowercase
    cleaned_text = ''  # create an empty string to store the filtered results
    for char in text:  # loop over each character in the sentence
        if char in morse_code:  # check if the character is in the morse_code dictionary
            cleaned_text = cleaned_text + char  # if it is a valid character, append it to cleaned_text
        elif char == ' ':
            cleaned_text = cleaned_text + char  # if it is a space, it is also appended to cleaned_text
    return cleaned_text  # return the filtered sentences


# convert a sentence entered by the user into a list of Morse codes
def convert_to_morse(text):
    filtered = filter_input(text)  # call the filter_input function to filter out invalid characters
    words = filtered.split(' ')  # split the filtered sentences into word lists by spaces
    morse_list = []  # create an empty list to store Morse code

    for word in words:  # loop over each word
        for char in word:  # loop over each character in a word
            morse_list.append(morse_code[char])  # ddd the Morse code for each character to the list
        morse_list.append('/')  # add / after each word's Morse code to indicate the end of the word

    return morse_list[:-1]  # return the Morse code list, removing the last extra /


# accepts two parameters
def play_morse(morse_list, unit_time):
    color = (0, 25, 0)  # set the LED light color to green

    for code in morse_list:  # loop over each morse code in morse_list
        if code == '/':
            cp.pixels.fill((0, 0, 0))  # turn off all LED lights
            time.sleep(7 * unit_time)  # wait 7 time units
        else:
            for symbol in code:  # loop over each symbol (dot or dash) in Morse code
                if symbol == '.':
                    cp.pixels.fill(color)  # turn on all LED lights
                    time.sleep(unit_time)  # wait 1 time unit
                    cp.pixels.fill((0, 0, 0))  # turn off all LED lights

                elif symbol == '-':
                    cp.pixels.fill(color)  # turn on all LED lights
                    time.sleep(3 * unit_time)  # wait 3 time unit
                    cp.pixels.fill((0, 0, 0))  # turn off all LED lights

                time.sleep(unit_time)  # wait 1 unit of time between symbols
            time.sleep(3 * unit_time)  # wait 3 units of time between characters


if __name__ == '__main__':
    unit_time = get_time()  # call the get_time function to get the unit time entered by the user
    sentence = input('Please enter a sentence: ')  # let the user enter a sentence
    morse_list = convert_to_morse(sentence)  # call the convert_to_morse function to convert the sentence into a list of Morse code
    print('Morse Code:', morse_list)  # print Morse code list
    play_morse(morse_list, unit_time)  # call the play_morse function to display Morse code through the CPX LED light

