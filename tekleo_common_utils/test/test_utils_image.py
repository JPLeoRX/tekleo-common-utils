# Run dependency injections
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_image import UtilsImage

u = UtilsImage()
u.download_image_pil('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/2006-2009_Honda_Civic_VTi-L_sedan_01.jpg/640px-2006-2009_Honda_Civic_VTi-L_sedan_01.jpg')
