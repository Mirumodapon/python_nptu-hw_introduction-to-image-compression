from cv2 import imread, imwrite
from cv2 import cvtColor, COLOR_BGR2GRAY
from cv2 import threshold, THRESH_BINARY

inputFile = input('Please enter input file path(Default: input.png): ')
grayOutputFile = input('Please enter gray image output path(Default: gray.png): ')
binaryOutputFile = input('Please enter binary image output path(Default: binary.png): ')


img = imread(inputFile if inputFile != '' else 'input.png')

gray = cvtColor(img, COLOR_BGR2GRAY)

info, binary = threshold(gray, 127, 255, THRESH_BINARY)


imwrite(grayOutputFile if grayOutputFile != '' else 'gray.png', gray)
imwrite(binaryOutputFile if binaryOutputFile != '' else 'binary.png', binary)

print('Complete.')
