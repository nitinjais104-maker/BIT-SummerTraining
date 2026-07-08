# Day 2 Assignment solution for Rohan Nishad

# 1. Check whether a number is positive, negative, or zero.
def check_number(value: int) -> str:
    if value > 0:
        return "Positive"
    if value < 0:
        return "Negative"
    return "Zero"

# 2. Check whether a number is even or odd.
def check_even_odd(value: int) -> str:
    return "Even" if value % 2 == 0 else "Odd"

# 3. Create a list of 10 numbers and print each number using a loop.
numbers = [5, 12, 7, 9, 20, 33, 44, 51, 68, 71]

# 4. Function to calculate average of 3 marks.
def calculate_average(mark1: float, mark2: float, mark3: float) -> float:
    return (mark1 + mark2 + mark3) / 3

# 5. Function to print grade based on marks.
def grade_student(marks: float) -> str:
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"

# Example usage and output for the assignment.
if __name__ == "__main__":
    print("Number check for 10:", check_number(10))
    print("Number check for -5:", check_number(-5))
    print("Number check for 0:", check_number(0))
    print("Even/Odd check for 11:", check_even_odd(11))
    print("Even/Odd check for 24:", check_even_odd(24))

    print("List of 10 numbers:")
    for num in numbers:
        print(num)

    average_marks = calculate_average(85, 92, 78)
    print("Average marks:", average_marks)
    print("Grade for average marks:", grade_student(average_marks))

    print("Grade for 95:", grade_student(95))
    print("Grade for 70:", grade_student(70))
    print("Grade for 50:", grade_student(50))
    print("Grade for 30:", grade_student(30))
