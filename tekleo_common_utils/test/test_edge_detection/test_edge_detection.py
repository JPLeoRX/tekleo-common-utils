# Run dependency injections
import cv2
import numpy as np
from injectable import load_injection_container
load_injection_container('../../')
from tekleo_common_utils.utils_image import UtilsImage
from tekleo_common_utils.utils_opencv import UtilsOpencv

utils_image = UtilsImage()
utils_opencv = UtilsOpencv()

# image_pil = utils_image.open_image_pil("nfs_5ca53a1494845a13003fc661.jpg")
image_pil = utils_image.open_image_pil("45 degree 12.jpeg")
image_cv = utils_image.convert_image_pil_to_image_cv(image_pil)
utils_image.debug_image_cv(image_cv)

image_gray_cv = utils_opencv.convert_to_grayscale(image_cv)
image_blurred_cv = utils_opencv.blur_gaussian(image_gray_cv, 3, 3)
utils_image.debug_image_cv(image_blurred_cv)

imgt = cv2.Canny(image_blurred_cv, 30, 240)
# imgt = cv2.adaptiveThreshold(image_blurred_cv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 11)
# ret, imgt = cv2.threshold(image_blurred_cv, 0, 255, cv2.THRESH_BINARY)
utils_image.debug_image_cv(imgt)
contours, hierarchy = cv2.findContours(imgt, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)
image_cv = cv2.drawContours(image_cv, contours, -1, (0, 255, 0), 3)
utils_image.debug_image_cv(image_cv)
exit(-1)

new_contours = []
min_area = image_pil.width * image_pil.height * 0.3 / 100
print('min area =', min_area)
for contour in contours:
    area = cv2.contourArea(contour)
    print('area =', area)
    if area > 200:
        peri = cv2.arcLength(contour, True)
        big_contour = cv2.approxPolyDP(contour, 0.001 * peri, True)
        new_contours.append(big_contour)

image_cv = cv2.drawContours(image_cv, new_contours, -1, (0, 255, 0), 3)
utils_image.debug_image_cv(image_cv)
exit(-1)

# Using the Canny filter to get contours
image_edges_low_thresh_cv = cv2.Canny(image_blurred_cv, 20, 30)
utils_image.debug_image_cv(image_edges_low_thresh_cv)

# Using the Canny filter with different parameters
image_edges_high_thresh_cv = cv2.Canny(image_blurred_cv, 60, 120)
utils_image.debug_image_cv(image_edges_high_thresh_cv)

sobelx = cv2.Sobel(src=image_blurred_cv, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
utils_image.debug_image_cv(sobelx)
sobely = cv2.Sobel(src=image_blurred_cv, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
utils_image.debug_image_cv(sobely)
sobelxy = cv2.Sobel(src=image_blurred_cv, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
utils_image.debug_image_cv(sobelxy)

# def auto_canny_edge_detection(image, sigma=0.33):
#     md = np.median(image)
#     lower_value = int(max(0, (1.0-sigma) * md))
#     upper_value = int(min(255, (1.0+sigma) * md))
#     return cv2.Canny(image, lower_value, upper_value)

# image_edges_cv = auto_canny_edge_detection(image_blurred_cv)
# utils_image.debug_image_cv(image_edges_cv)