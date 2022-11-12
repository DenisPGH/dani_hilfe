
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
speaker.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

screenshot='screen_/screen.jpg'

y_first=380
h_first=20
x_first=0
w_first=170

# origin
img = cv2.imread(f"{screenshot}")
# get only one rolete
crop_img = img[y_first:y_first+h_first, x_first:x_first+w_first]
img=cv2.resize(crop_img, (180, 30), interpolation = cv2.INTER_LINEAR)
img = cv2.bitwise_not(img)
#img=crop_img

# start bearbeitung

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convert the image to gray scale
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)# Performing OTSU threshold
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1)) #10,10
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
found_wors=[]
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    text = pytesseract.image_to_string(cropped)
    found_wors.append(text)




print(found_wors)
#text=f"{len(found_wors)} found sentenses. They are: {', '.join(found_wors)}"
# speaker.say(text)
# speaker.runAndWait()



cv2.imshow("cropped", im2)
cv2.waitKey(0)
