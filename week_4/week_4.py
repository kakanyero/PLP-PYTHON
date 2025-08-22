filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        modified_content = content.upper()  # modify the content

    # write the modified content to a new file
    new_filename = f"modified_{filename}"
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")

except Exception as e:
    print(f"An error occurred: {e}")
