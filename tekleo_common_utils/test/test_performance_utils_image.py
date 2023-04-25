# Run dependency injections
import time
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_image import UtilsImage

u = UtilsImage()

t1 = time.time()
#image_pil = u.open_image_pil("image_rotate_+4.65.jpg", rotate_to_exif_orientation=True)
image_pil = u.open_image_pil("IMG_4664.JPG", rotate_to_exif_orientation=True)
print(image_pil.getexif())
t2 = time.time()
td = round(t2 - t1, 3)
print('Image opening with rotation took ' + str(td) + ' seconds')

t1 = time.time()
u.save_image_pil(image_pil, "tttttt1.JPG", quality=90, subsampling=1)
t2 = time.time()
td = round(t2 - t1, 3)
print('Image saving took ' + str(td) + ' seconds')

u.debug_image_pil(image_pil)
# image_pil = u.rotate_image_according_to_exif_orientation(image_pil)
# u.debug_image_pil(image_pil)