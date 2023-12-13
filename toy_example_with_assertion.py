from pathlib import Path
from tempfile import TemporaryDirectory
import string
import random

# Some toy examples of testing without pytest, but still very useful.
# Mainly assert
x = 1 + 1
assert x == 2


# Test function gives the right output
# Useful for corner cases or sense checking with known values.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


for temperature in [32, 212, -459.67]:
    if temperature == 32:  # Freezing point of water
        assert fahrenheit_to_celsius(temperature) == 0.0
    elif temperature == 212:  # Boiling point
        assert fahrenheit_to_celsius(temperature) == 100
    elif temperature == -459.67:  # Absolute zero
        assert fahrenheit_to_celsius(temperature) == -273.15
    else:
        pass


# Making sure an input value is the expected type
value = input("Please provide the age for your dog, only numbers..")
age = int(value)
assert isinstance(age, int)


# When creating or modifying filenames and you need to check they are of an specific extension
def generate_random_file_name():
    dictionary = string.ascii_letters + string.digits
    random_name = "".join(random.choice(dictionary) for _ in range(10))
    return random_name + ".pdf"


with TemporaryDirectory() as td:
    td = Path(td)

    # Check for 10 random files
    for _ in range(10):
        filename = generate_random_file_name()
        assert filename.endswith(".pdf")

        # Let's check also the path is also correct
        # btw the pathlib package is super useful.
        filepath = td / filename
        assert filepath.suffix == ".pdf"

        # BTW can also assert value not
        assert filepath.suffix != ".png"
