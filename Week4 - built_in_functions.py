print("Program Started!")
print("Please enter a Standard Character")
character = input()

if len(character) ==1:
    code = ord(character)
    print(f"The ASCII code for {character} is {code}.")
print("Program Ended!")
