# Run dependency injections
from injectable import load_injection_container
load_injection_container('../../')
from tekleo_common_utils.utils_image import UtilsImage


utils = UtilsImage()

utils.debug_image_metadata('IMG_4404.jpg')
utils.debug_image_metadata('IMG_9163.jpg')
utils.debug_image_metadata('IMG_9798.jpg')
