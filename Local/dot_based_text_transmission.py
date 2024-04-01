import cv2
from time import sleep


# Camera options
LAPTOP_CAMERA = 1
EXTERNAL_CAMERA = 0

SHOW_CAMERA_FEED = False

# Time to wait before performing the next OCR
WAIT_TIME = 0.125

# This array contains symbols, their position in the array is the number of dots (B === 3)
SYMBOL_MAP = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",", "!", "?", ":", ";", 
                "(", ")", "[", "]", "{", "}", "<", ">", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "/", "\\", "|", "`", "~", "'", '"', 
                "鳳", "端", "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú", "ñ", "Ñ", "¿", "¡", "ä", "Ä", "ë", "Ë", "ï", "Ï", "ö", "Ö", "ü", "Ü"]

temp_file_contents = ""

def save_last_symbol(symbol, force_save=False):
    # Rules:
    # Duplicates in the file means that the symbol was detected more than once,
    # but if not followed by "端", it's a capture error, not a duplicate

    global temp_file_contents
    temp_file_contents += symbol
    
    if len(temp_file_contents) > 100 or symbol == "端" or force_save:
        with open("decryption_end.txt", "a+", encoding="utf8") as file:
            file.write(temp_file_contents)
        temp_file_contents = ""

def decrypt_symbol(number_value):
    if number_value < 0 or number_value > SYMBOL_MAP.__len__() - 1:
        return "侶"
    return SYMBOL_MAP[number_value]

def count_dots_from_webcam():
    cap = cv2.VideoCapture(EXTERNAL_CAMERA)
    print("starting...")
    for i in range(3):
        print(f"{3 - i}...")
        sleep(1)
    print("started\n")

    while True:
        if not cap.isOpened():
            print("Error: Could not access the webcam.")
            return
        
        sleep(WAIT_TIME)

        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        num_dots = len(contours)

        symbol = decrypt_symbol(num_dots)
        save_last_symbol(symbol)

        print(f"Dots: {num_dots} --> Symbol: {symbol}")

        if SHOW_CAMERA_FEED:
            cv2.putText(frame, f"Dots: {num_dots}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Webcam Dots Counter', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

count_dots_from_webcam()
