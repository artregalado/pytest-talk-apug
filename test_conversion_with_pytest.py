import pytest
import cv2 as cv
import numpy as np


# Function declaration - can be in another file as long as is imported into the namspace
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Vanilla (bruteforce) testing with pytest.... lots of repetition
# Also note to pytest.raises to showcase that it can catch exceptions and ensure they are raised.


# Test for the freezing point of water (32°F to 0°C)
def test_freezing_point_of_water():
    result = fahrenheit_to_celsius(32)
    assert result == 0


# Test for the boiling point of water (212°F to 100°C)
def test_boiling_point_of_water():
    result = fahrenheit_to_celsius(212)
    assert result == 100.0


# Test for absolute zero (-459.67°F to -273.15°C)
def test_absolute_zero():
    result = fahrenheit_to_celsius(-459.67)
    assert result == -273.15


# Additional test for invalid input (eg. string input)
def test_fahrenheit_to_celsius_invalid_input():
    with pytest.raises(Exception):
        fahrenheit_to_celsius("invalid_input")


# Showcase parametrize - look how simpler to read and also to test
# Remember to speak about the different scopes
# Note the decorator beginning with @
# In this case, the scope of parametrize is the next function call,
# but different scope levels can be defined.


@pytest.mark.parametrize(
    argnames="input_fahrenheit, expected_celsius",
    argvalues=[
        (32, 0.0),  # Freezing point of water
        (212, 100),  # Boiling point
        (-459.67, -273.15),  # Absolute zero
    ],
)
def test_conversion_parametrized(input_fahrenheit, expected_celsius):
    result = fahrenheit_to_celsius(input_fahrenheit)
    assert result == expected_celsius


## Showcase the use of classes as means to organizing the testing
# Define a test class
class TestFahrenheitToCelsiusConversion:
    # Test for the freezing point of water (32°F to 0°C)
    def test_freezing_point_of_water(self):
        result = fahrenheit_to_celsius(32)
        assert result == 0.0

    # Test for the boiling point of water (212°F to 100°C)
    def test_boiling_point_of_water(self):
        result = fahrenheit_to_celsius(212)
        assert result == 100.0

    # Test for absolute zero (-459.67°F to -273.15°C)
    def test_absolute_zero(self):
        result = fahrenheit_to_celsius(-459.67)
        assert result == -273.15

    # Additional test for invalid input (string input)
    def test_fahrenheit_to_celsius_invalid_input(self):
        with pytest.raises(Exception):
            fahrenheit_to_celsius("invalid_input")


# Now use pytest fixture to show how we can upload a file and avoid repetition.
# Imagine having to test functions that process an image. Instead of having to load the image in each test, we can create a fixture, and it will be available for the chosen scope.


@pytest.fixture
def sample_image():
    image = cv.imread("sample_image.jpg", cv.IMREAD_GRAYSCALE)
    yield image


# Test function to apply binarization to the sample image
def test_image_binarization(sample_image):
    # Apply binarization using a threshold value
    _, binarized_image = cv.threshold(sample_image, 127, 255, cv.THRESH_BINARY)

    unique_values = np.unique(binarized_image)
    assert len(unique_values) == 2  # There should be only 2 unique values
    assert 0 in unique_values  # 0 should be one of the unique values
    assert 255 in unique_values  # 255 should be the other unique value


# Test function to apply simple blurring filter to the sample image
def test_image_blur(sample_image):
    # Apply simple blurring filter
    blurred_image = cv.GaussianBlur(sample_image, (5, 5), 0)
    # To test if the image is actually blurred, compare it to the original image and check for differences in pixel values. When an image is blurred, the pixel values in the blurred image should be different from the original image.

    # Perform assertions on the blurred image
    mse = np.mean((sample_image - blurred_image) ** 2)
    threshold = 5

    # Check if the MSE is greater than the threshold to indicate blurriness
    assert mse > threshold
