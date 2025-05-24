import cv2
import pytesseract
import pyautogui
import numpy as np
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def screen_capture():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    area_of_interest = screenshot[475:590, 1600:1920]
    
    return area_of_interest

def detect_numbers(image, numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
    text = pytesseract.image_to_string(image)
    detected_numbers = [num for num in numbers if num in text]
    return detected_numbers

def main():
    number_detected = {str(i): False for i in range(1, 10)}

    while True:
        image = screen_capture()
        
        detected = detect_numbers(image)

        for num in detected:
            if not number_detected[num]:
                print(f"Found {num}, typed!")
                time.sleep(0.5)
                pyautogui.write(num)
                number_detected[num] = True
        
        for num in number_detected:
            if num not in detected and number_detected[num]:
                print(f"{num} disappeared, researching...")
                number_detected[num] = False

        time.sleep(1)
if __name__ == "__main__":
    main()
