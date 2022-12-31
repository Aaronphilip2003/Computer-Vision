import cv2 as cv

def rescale(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread("C:\Computer Vision\icons8-bones-64.png")
img=rescale(img,scale=0.50)


def convertGrey(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return gray

def gaussianBlur(img):
    blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
    return blur

def cannyEdges(img):
    canny=cv.Canny(img,100,100)
    return canny

def dilate(img):
    dilated=cv.dilate(img,(7,7),iterations=3)
    return dilate

# cv.imshow("Schumacher",img)
bnw=cv.imshow("Grayscale",convertGrey(img))
# cv.imshow("Blur",gaussianBlur(img))
# cv.imshow("Canny",cannyEdges(img))
# cv.imshow("Cropped",img[100:300,100:300])
cv.imwrite(".png",bnw)

cv.waitKey(0)