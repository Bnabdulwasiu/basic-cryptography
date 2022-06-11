from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text_answer, shift_answer, direction_answer):
    
    end_text = ""
    for char in text_answer:
        if char in alphabet:
            if direction_answer == "encode":
                letter_index = alphabet.index(char)
                new_position = letter_index + shift_answer
                new_letter = alphabet[new_position]
                end_text += new_letter
                
            elif direction_answer == "decode":
                letter_index = alphabet.index(char)
                new_position = letter_index - shift_answer
                new_letter = alphabet[new_position]
                end_text += new_letter
            
            else:
                "Print wrong input"
        else:
            end_text += char    
    print(f"The {direction_answer}d text is: {end_text}")


quit = False
while quit == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(text_answer=text, shift_answer=shift, direction_answer=direction)
    message  = input("Type 'yes' if you want to go agian. Otherwise type 'no'. ").lower()
    if message == 'no':
        quit = True
        print("Goodbye")