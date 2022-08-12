# Run dependency injections
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_image import UtilsImage

u = UtilsImage()

# Test download
u.download_image_pil('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/2006-2009_Honda_Civic_VTi-L_sedan_01.jpg/640px-2006-2009_Honda_Civic_VTi-L_sedan_01.jpg')

# Test Exif (JPG)
image_pil = u.open_image_pil("IMG_9798.JPG")
print(image_pil.getexif())
image_without_exif_pil = u.clear_exif_data(image_pil)
print(image_without_exif_pil.getexif())
image_without_exif_pil.save("IMG_9798_NO_EXIF.JPG")

# Test Exif (HEIC)
image_pil = u.open_image_pil("IMG_8629.HEIC")
print(image_pil.getexif())
image_without_exif_pil = u.clear_exif_data(image_pil)
print(image_without_exif_pil.getexif())
image_without_exif_pil.save("IMG_8629_NO_EXIF.HEIC")

# Test conversion
u.convert_to_jpg("image_rotate_+4.65.png")
u.convert_to_jpg("IMG_8629.HEIC")