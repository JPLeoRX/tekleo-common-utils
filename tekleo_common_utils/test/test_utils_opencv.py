# # Run dependency injections
import os
import tekleo_common_utils
from injectable import load_injection_container
# load_injection_container(str(os.path.dirname(tekleo_common_utils.__file__)))
load_injection_container('../')

from tekleo_common_utils.utils_image import UtilsImage
from tekleo_common_utils.utils_opencv import UtilsOpencv


utils_image = UtilsImage()
utils_opencv = UtilsOpencv()


def test_rotation_1():
    image_cv = utils_image.open_image_cv('image_rotate_+4.65.png')
    image_bound = utils_opencv.rotate_bound(image_cv, -4.65)
    image_free = utils_opencv.rotate_free(image_cv, -4.65)

    utils_image.debug_image_cv(image_cv, 'Image Original')
    utils_image.debug_image_cv(image_bound, 'Rotated Bound')
    utils_image.debug_image_cv(image_free, 'Rotated Free')

    print(utils_opencv.get_dimensions_wh(image_cv))
    print(utils_opencv.get_dimensions_wh(image_bound))
    print(utils_opencv.get_dimensions_wh(image_free))


def test_rotation_2():
    image_cv = utils_image.open_image_cv('image_rotate_+90.png')
    image_bound = utils_opencv.rotate_bound(image_cv, 90)
    image_free = utils_opencv.rotate_free(image_cv, 90)

    utils_image.debug_image_cv(image_cv, 'Image Original')
    utils_image.debug_image_cv(image_bound, 'Rotated Bound')
    utils_image.debug_image_cv(image_free, 'Rotated Free')

    print(utils_opencv.get_dimensions_wh(image_cv))
    print(utils_opencv.get_dimensions_wh(image_bound))
    print(utils_opencv.get_dimensions_wh(image_free))


def test_brightness_and_contrast():
    image_cv = utils_image.open_image_cv('IMG_9798.JPG')
    image_cv = utils_opencv.brightness_and_contrast(image_cv, brightness=255, contrast=127)
    utils_image.debug_image_cv(image_cv)

def test_border():
    image_cv = utils_image.open_image_cv('IMG_9798.JPG')
    image_cv = utils_opencv.border(image_cv, 100, 0, 0, 0, (0, 0, 0))
    utils_image.debug_image_cv(image_cv)

def test_saturation():
    image_cv = utils_image.open_image_cv('IMG_9798.JPG')
    image_cv = utils_opencv.saturation(image_cv, saturation_coefficient=1.0)
    utils_image.debug_image_cv(image_cv)
    image_cv = utils_opencv.saturation(image_cv, saturation_coefficient=1.5)
    utils_image.debug_image_cv(image_cv)

def test_hue():
    image_cv = utils_image.open_image_cv('IMG_9798.JPG')
    image_cv = utils_opencv.hue(image_cv, hue_coefficient=1.0)
    utils_image.debug_image_cv(image_cv)
    # image_cv = utils_opencv.hue(image_cv, hue_coefficient=1.06)
    # utils_image.debug_image_cv(image_cv)
    image_cv = utils_opencv.hue(image_cv, hue_coefficient=0.94)
    utils_image.debug_image_cv(image_cv)

def test_sharpen():
    image_cv = utils_image.open_image_cv('IMG_9798.JPG')
    utils_image.debug_image_cv(image_cv)
    # image_cv_1 = utils_opencv.sharpen_blur(image_cv, sharpen_blur_x=105, sharpen_blur_y=105)
    # utils_image.debug_image_cv(image_cv_1)
    image_cv_2 = utils_opencv.sharpen_kernel(image_cv)
    utils_image.debug_image_cv(image_cv_2)

# test_rotation_1()
# test_rotation_2()
# test_brightness_and_contrast()
# test_border()
# test_hue()
test_sharpen()