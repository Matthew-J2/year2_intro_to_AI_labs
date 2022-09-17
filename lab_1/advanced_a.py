import random


def UNGoals(student_id):
    """Generates two integers with a different value between 1 and 17 based on a student's ID number.

    Args:
        student_id(int): The student's ID number.

    Returns:
        tuple: Two generated integers.
    """
    random.seed(a=student_id)
    num1 = random.randrange(1, 18)
    while True:
        num2 = random.randrange(1, 18)
        if num1 != num2:
            break
    return num1, num2


def main():
    while True:
        try:
            student_id = int(input("Please enter your Student ID number.\n"))
        except ValueError:
            print("Enter a number please.")
        else:
            (num1, num2) = UNGoals(student_id)
            print(f"Your first goal is {num1}, and your second goal is {num2}.")
            break


if __name__ == "__main__":
    main()

"""
stuff to reference:
https://docs.python.org/3/library/random.html#random.seed
https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
"""