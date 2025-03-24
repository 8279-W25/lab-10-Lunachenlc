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
