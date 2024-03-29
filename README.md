# supermarketsim_pricer
Python tool to set prices based on percentage markup

## Installation

1. Clone the repo
    ```bash
    git clone https://github.com/snalye/supermarketsim_pricer
    ```
2. Navigate to the project directory
    ```bash
    cd supermarketsim_pricer
    ```
3. Install the required dependencies using pip
    ```bash
    pip install pyautogui pillow pytesseract pyperclip keyboard opencv-python
    ```
4. Download tesseract-ocr from their github: https://github.com/UB-Mannheim/tesseract/wiki
## Usage

According to [this guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3171056543), set the percentage to 0-10% to avoid complaints

1. Update the config.ini file with the desired configuration parameters:

    - `tesseract_cmd`: Path to the Tesseract OCR executable.
    - `x1, y1, x2, y2`: Coordinates of the top-left and bottom-right corners of the region of     interest (ROI) on the screen. It is currently setup for a 1440p screen
    - Keybinds
        - `scan`: Key combination to trigger the price checking action via       screenshot. Default `ctrl+shift+a`
        - `manual`: Key comination to trigger the manual price checking.        Default `ctrl+shift+s`
        - `percentage`: Key comination to trigger the manual price checking. Default `ctrl+shift+x`
        - `exit`: Key combination to exit script. Default `tab`
2. Run the script:
    ```bash
    python main.py
    ```
3. Once the script is running, use the specified keybind (default is ctrl+shift+a) to trigger the price checking action. If no text is detected in the specified region, you'll be prompted to enter the price value manually.
4. The script will calculate the updated price with the specified percentage increase and copy it to your clipboard.

## Contributing

Contributions are welcome! This is my first python script so there may be better ways this can be accomplished. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
