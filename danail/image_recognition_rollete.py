
import cv2
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# screenshot='screen_/scr_1.png'
#
# y_first=830 #830
# x_first=640 # 50,640,1200
# h_first=70
# w_first=600
#
#
#
#
#
# # origin
# img = cv2.imread(f"{screenshot}")
# # get only one rolete
# crop_img = img[y_first:y_first+h_first, x_first:x_first+w_first]
# #img = cv2.bitwise_not(crop_img)
# img=crop_img
#
# # start bearbeitung
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convert the image to gray scale
# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)# Performing OTSU threshold
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1)) #10,10
# dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
#                                        cv2.CHAIN_APPROX_NONE)
# im2 = img.copy()
# found_wors=[]
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     cropped = im2[y:y + h, x:x + w]
#     text = pytesseract.image_to_string(cropped)
#     found_wors.append(text)
#
#
#
#
#
# only_digits=[]
# import re
# patern='(?P<num>([0-9]+|o))'
#
# for each in found_wors:
#     digits=re.finditer(patern,each)
#     for d in digits:
#         dd=d.group('num')
#         if dd=="o":
#             dd=0
#         else:
#             dd=int(dd)
#         only_digits.append(dd)
#
#
#
# print(only_digits)
# cv2.imshow("cropped", im2)
# cv2.waitKey(0)
#

class ImageRecognition:
    def __init__(self):
        self.PATTERN='(?P<num>([0-9]+|o))'
        self.ROLLETE_PIXELS = {1: [830, 50, 70, 600], 2: [830, 640, 70, 600], 3: [830, 1200, 70, 600]}
        self.MAX_NUM=36
        self.MIN_NUM=0
        # {wrong:write,}
        self.DICT_CORRECTION_WRONG_NUMBERS={380:30, 92:32}
        self.RED_GROUP=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.BLACK_GROUP=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


    def color_checker(self,number):
        """
        :param number:
        :return: color of the number from the given rolete values b=black, r=red
        """
        if number in self.RED_GROUP:
            return 'r'
        elif number in self.BLACK_GROUP:
            return 'b'
        elif number == 0:
            return  'rb'
        else:
            return 'rb'


    def wrong_value_checker(self,number):
        """
        if number is wrong, check for rigth and return it

        :param number: actual number
        :return: right number
        """
        if number >=self.MIN_NUM and number <=self.MAX_NUM:
            return number
        if number in self.DICT_CORRECTION_WRONG_NUMBERS:
            return  self.DICT_CORRECTION_WRONG_NUMBERS[number]
        else:
            return 0

    def regex_helper(self,source_detection:list):
        """
        used regex to detect only the numbers
        :param source_detection: list with found words and numbers
        :return: list with only integers numbers
        """
        only_digits = []
        self.PATTERN = '(?P<num>([0-9]+|o))'
        for each in source_detection:
            digits = re.finditer(self.PATTERN, each)
            for d in digits:
                dd = d.group('num')
                if dd == "o":
                    dd = 0
                else:
                    dd = int(dd)
                only_digits.append(dd)

        return only_digits


    def return_numbers_from_screenshot(self,source_picture,y_first,x_first,h_first,w_first):
        """

        :param source_picture: path to the source picture
        :param y_first: y value
        :param x_first: x value
        :param h_first: abstand from y
        :param w_first: abstand from x
        :return: list with found words
        """

        # origin
        img = cv2.imread(f"{source_picture}")
        # get only one rolete
        crop_img = img[y_first:y_first + h_first, x_first:x_first + w_first]
        img = cv2.bitwise_not(img)
        img = crop_img

        # start bearbeitung

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to gray scale
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)  # Performing OTSU threshold
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))  # 10,10
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        im2 = img.copy()
        found_wors = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = im2[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)
            found_wors.append(text)
        res=self.regex_helper(found_wors)
        return res


    def main_function(self,screenshot_path='screen_/scr_1.png',):
        dict_with_values = {1: [], 2: [], 3: []}
        for rol, values in self.ROLLETE_PIXELS.items():
            y = values[0]
            x = values[1]
            h = values[2]
            w = values[3]
            res = self.return_numbers_from_screenshot(screenshot_path, y, x, h, w)
            current_number_serie=[]
            for number in res[:8]:
                number=self.wrong_value_checker(number) # check if it wrong
                color=self.color_checker(number)
                current_number_serie.append((number,color))
            dict_with_values[rol] = current_number_serie  # store only the last 8 numbers
        return  dict_with_values




if __name__=="__main__":
    ir=ImageRecognition()
    a=ir.main_function()
    print(a)


