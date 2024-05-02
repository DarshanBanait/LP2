def modify_string(input_string):
    result = []
    mask = 127  # Binary: 0b01111111

    for char in input_string:
        # Perform bitwise AND with 127
        and_result = ord(char) & mask

        # Perform bitwise XOR with 127
        xor_result = ord(char) ^ mask

        # Append the modified characters to the result list
        result.append((char, and_result, xor_result))

    return result

def display_results(modified_results):
    print("Character\tAND Result\tXOR Result")
    print("---------------------------------------")
    for char, and_res, xor_res in modified_results:
        print(f"{char}\t\t{and_res}\t\t{xor_res}")

def main():
    input_string = "Hello World"

    # Modify each character in the input string
    modified_results = modify_string(input_string)

    # Display the modified results
    display_results(modified_results)

if __name__ == "__main__":
    main()
