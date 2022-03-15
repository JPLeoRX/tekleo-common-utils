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


test_rotation_1()
test_rotation_2()