import configparser
import pyautogui
from PIL import Image
import pytesseract
import re
import pyperclip
import keyboard
import cv2

config = configparser.ConfigParser()
config.read('config.ini')
pytesseract.pytesseract.tesseract_cmd = config['General']['tesseract_cmd']

def changePercentage():
    global increase_percentage
    increase_percentage = int(input('Enter percentage for price: '))
    print(f"Percentage set to: {increase_percentage}%")
    print("Waiting for scan...")

changePercentage()

def grayscale(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray_image
def action():

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save('temp/screenshot.jpg')

    # Coordinates of the top-left corner of the ROI
    left = int(config['General']['x1'])
    upper = int(config['General']['y1'])

    # Coordinates of the bottom-right corner of the ROI
    x2 = int(config['General']['x2'])
    y2 = int(config['General']['y2'])

    # Calculate width and height of the ROI
    width = x2 - left
    height = y2 - upper

    # Define the cropping box
    right = left + width
    lower = upper + height

    # Crop the screenshot
    cropped_screenshot = screenshot.crop((left, upper, right, lower))
    cropped_screenshot.save('temp/screenshot_crop.jpg')

    image_path = 'temp/screenshot_crop.jpg'

    gray_image = grayscale(image_path)
    cv2.imwrite('temp/gray.jpg', gray_image)

    thresh, im_bw = cv2.threshold(gray_image, 190, 230, cv2.THRESH_BINARY)
    cv2.imwrite("temp/bw_image.jpg", im_bw)

    image = Image.open('temp/bw_image.jpg')
    try:
        # Perform OCR and text processing steps
        extracted_text = pytesseract.image_to_string(image)

        if extracted_text.strip() == '':
            # If no text is detected, prompt the user for input from the command line
            extracted_text = input("Enter the price value manually: ")

        # Remove non-numeric characters except decimal point
        extracted_text = re.sub(r'[^\d.]+', '', extracted_text)

        # Convert the extracted text to a float
        price_value = float(extracted_text)

        # Apply formatting rules
        formatted_price = "{:.2f}".format(price_value)  # Format as currency with two decimal places
        price = float(formatted_price)

        # Price Math
        increase_amount = (increase_percentage / 100.0) * price
        new_price = round(price + increase_amount, 2)
        new_price_str = "{:.2f}".format(new_price)
        print("Original Price:", price)
        print(f"{increase_percentage}% Increase:", new_price)
        pyperclip.copy(new_price_str)
    except Exception as e:
        # Handle OCR errors or processing failures
        print("Error:", e)
# # Keybind to activate photo

def manual():
    extracted_text = input("Enter the price value manually: ")

    # Remove non-numeric characters except decimal point
    extracted_text = re.sub(r'[^\d.]+', '', extracted_text)
    # Convert the extracted text to a float
    price_value = float(extracted_text)
    # Apply formatting rules
    formatted_price = "{:.2f}".format(price_value)  # Format as currency with two decimal places
    price = float(formatted_price)
    # Price Math
    increase_amount = (increase_percentage / 100.0) * price
    new_price = round(price + increase_amount, 2)
    new_price_str = "{:.2f}".format(new_price)
    print("Original Price:", price)
    print(f"{increase_percentage}% Increase:", new_price)
    pyperclip.copy(new_price_str)


# Keybing to activate manual
keyboard.add_hotkey(config['Keybind']['manual'], manual)

keyboard.add_hotkey(config['Keybind']['scan'], action)


keyboard.add_hotkey(config['Keybind']['percentage'], changePercentage)

keyboard.wait(config['Keybind']['exit'])