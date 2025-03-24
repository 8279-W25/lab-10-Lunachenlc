morse_code = {
    'a':'.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8' : '---..', '9':'----.'
}

#convert the sentence to lowercase and remove any character without a Morse code equivalent
def filter_input(text):
    text = text.lower()     #convert the sentence to lowercase
    cleaned_text = ''       #create an empty string to store the filtered results
    for char in text:       #loop over each character in the sentence
        if char in morse_code:      #check if the character is in the morse_code dictionary
            cleaned_text = cleaned_text + char      #if it is a valid character, append it to cleaned_text
        elif char == ' ':
            cleaned_text = cleaned_text + char      #if it is a space, it is also appended to cleaned_text
    return cleaned_text     #return the filtered sentences

sentence = input('Please enter a sentence: ')   #let the user enter a sentence
filtered = filter_input(sentence)       #call the filter_input function to filter the sentences entered by the user
print('Filtered sentence:', filtered)   #print the filtered sentences


#convert a sentence entered by the user into a list of Morse codes
def convert_to_morse(text):
    filtered = filter_input(text)       #call the filter_input function to filter out invalid characters
    words = filtered.split(' ')         #split the filtered sentences into word lists by spaces
    morse_list = []     #create an empty list to store Morse code

    for word in words:      #loop over each word
        for char in word:   #loop over each character in a word
            morse_list.append(morse_code[char])     #ddd the Morse code for each character to the list
        morse_list.append('/')      #add / after each word's Morse code to indicate the end of the word

    return morse_list[:-1]      #return the Morse code list, removing the last extra /

sentence = input('Please enter a sentence: ')      #let the user enter a sentence
morse_list = convert_to_morse(sentence)       #call the convert_to_morse function to convert the sentence into a list of Morse code
print('Morse Code:', morse_list)              #print Morse code list

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
            print('Invalid input. ')  #if the input is a non-numeric, let the user to re-enter

#get the GRB value (0-255) entered by the user and ensure that the input is valid
def get_color():
    while True:     # use while loop until the user enters a correct value
        try:
            red = int(input('Please enter the red value (0-255): '))
            green = int(input('Please enter the green value (0-255): '))
            blue = int(input('Please enter the blue value (0-255): '))
            if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:  # checks if the input value is between 0 and 255
                return (red, green, blue)  # if valid, returns the RGB value
            else:
                print('Values must be 0-255. Please try again.')   # if invalid, let the user to re-enter
        except ValueError:
            print('Invalid input. Please enter numbers.')   #if the input is a non-numeric, let the user to re-enter