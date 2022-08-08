# Run dependency injections
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_image import UtilsImage

u = UtilsImage()

# Test download
u.download_image_pil('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/2006-2009_Honda_Civic_VTi-L_sedan_01.jpg/640px-2006-2009_Honda_Civic_VTi-L_sedan_01.jpg')

# Test Exif
image_pil = u.open_image_pil("IMG_9798.JPG")
image_without_exif_pil = u.clear_exif_data(image_pil)
print(image_pil.getexif())
print(image_without_exif_pil.getexif())