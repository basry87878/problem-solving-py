def compressedString(message):
    # Initialize an empty result string
    result = ''
    
    # Initialize the counter and previous character
    counter = 1
    previous_char = message[0] if message else ''
    
    # Loop through the message starting from the second character
    for i in range(1, len(message)):
        current_char = message[i]
        
        if current_char == previous_char:
            # If the current character is the same as the previous one, increment the counter
            counter += 1
        else:
            # Append the previous character and the counter (if greater than 1) to the result
            result += previous_char
            if counter > 1:
                result += str(counter)
            
            # Reset the counter and update the previous character
            previous_char = current_char
            counter = 1
    
    # Append the last character and its count (if greater than 1) to the result
    result += previous_char
    if counter > 1:
        result += str(counter)
    
    return result

# Example usage
print(compressedString("Baasssryy"))   
