from problem3 import caesar_decrypt
 
def process_file(filename): 
    """Read, sort and return a file""" 
    with open(filename, 'r') as file: 
        file_text = file.read()
        clean_text = file_text.strip()
        sorted_items = sorted(clean_text.split())
        number_of_lines = file_text.count('\n')

        # Return a tuple
        return filename, sorted_items, number_of_lines

message = input("Please enter message: ")
filename = "common_words.txt"
dictionary = set(process_file(filename)[1])

#Function used to find out the correct message
def find_message(message):
    for i in range(1,26):
        potiential_message = caesar_decrypt(i, message).split()
        if any(word in dictionary for word in potiential_message):
            print(f"key is {i}")
            return caesar_decrypt(i, message)
    
try:
    print(find_message(message))
except: 
    print("WRONG!!!")
    
