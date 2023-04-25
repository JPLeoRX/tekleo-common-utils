# Run dependency injections
import time
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_image import UtilsImage

u = UtilsImage()

image_pil = u.open_image_pil("logo.svg", rotate_to_exif_orientation=True)
u.debug_image_pil(image_pil)
u.save_image_pil(image_pil, "logo.jpg")

image_pil = u.open_image_pil("Google_Colaboratory_SVG_Logo.svg", rotate_to_exif_orientation=True)
u.debug_image_pil(image_pil)
u.save_image_pil(image_pil, "Google_Colaboratory_SVG_Logo.jpg")

image_pil = u.open_image_pil("bla.svg", rotate_to_exif_orientation=True)
u.debug_image_pil(image_pil)
u.save_image_pil(image_pil, "bla.jpg")

image_pil = u.open_image_pil("280x178_2.svg", rotate_to_exif_orientation=True)
u.debug_image_pil(image_pil)
u.save_image_pil(image_pil, "280x178_2.jpg")

image_pil = u.open_image_pil("Honda.svg", rotate_to_exif_orientation=True)
u.debug_image_pil(image_pil)
u.save_image_pil(image_pil, "Honda.jpg")


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM
# drawing = svg2rlg("280x178_2.svg")
# pil_img = renderPM.drawToPILP(drawing)
#
# u.debug_image_pil(pil_img)

#
# t1 = time.time()
# image_pil = u.open_image_pil("image_rotate_+4.65.jpg", rotate_to_exif_orientation=True)
# #image_pil = u.open_image_pil("IMG_4664.JPG", rotate_to_exif_orientation=True)
# print(image_pil.getexif())
# t2 = time.time()
# td = round(t2 - t1, 3)
# print('Image opening with rotation took ' + str(td) + ' seconds')
#
# t1 = time.time()
# u.save_image_pil(image_pil, "tttttt1.JPG", quality=90, subsampling=1)
# t2 = time.time()
# td = round(t2 - t1, 3)
# print('Image saving took ' + str(td) + ' seconds')
#
# u.debug_image_pil(image_pil)
# # image_pil = u.rotate_image_according_to_exif_orientation(image_pil)
# # u.debug_image_pil(image_pil)