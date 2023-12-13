# See https://adventofcode.com/2023/day/1
# Instructions:
# I will give you the solution.
# Test the function and solutions with pytest.
# So we are working on testing an already implemented funcionality.
# You can also try your approach before using my solution.

import re


def extract_digits(line):
    # Define a dictionary to map spelled-out digits to their numerical values
    digit_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # Use a regular expression to find all spelled-out digits or numerical digits
    digits = re.findall(
        r"(?:zero|one|two|three|four|five|six|seven|eight|nine|\d+)", line
    )

    # Join the extracted digits and convert them to numerical values
    digits = "".join([digit_map.get(digit, digit) for digit in digits])

    # Extract the first and last digits
    first_digit = digits[0]
    last_digit = digits[-1]
    concatenated = "".join([first_digit, last_digit])

    return int(concatenated)


# Read the calibration document from a file or provide it as a list of strings
with open("input2.txt", "r") as file:
    lines = [line.strip() for line in file]

# Calculate the calibration values and sum them up

calibration_values = []
for line in lines:
    x = extract_digits(line)
    calibration_values.append(x)


total_calibration_value = sum(calibration_values)

print("Total Calibration Value:", total_calibration_value)
