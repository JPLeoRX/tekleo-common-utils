# Run dependency injections
from injectable import load_injection_container
load_injection_container('../../')
from tekleo_common_utils.utils_image import UtilsImage
from PIL.ExifTags import TAGS


u = UtilsImage()

def print_exif_data(exif_data):
    if exif_data is None:
        return
    else:
        for tag_id in exif_data:
            tag = TAGS.get(tag_id, tag_id)
            content = exif_data.get(tag_id)
            if isinstance(content, bytes):
                try:
                    content = content.decode()
                except:
                    content = 'ERROR'
            print(f'\t{tag:25}: {content}')

def format_dms_coordinates(coordinates):
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = (coordinates[0].num / coordinates[0].den) + (coordinates[1].num / coordinates[1].den) / 60 + (coordinates[2].num / coordinates[2].den) / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees

# Open image
# image_pil = u.open_image_pil("IMG_9163.jpg", rotate_to_exif_orientation=False)
# print('Main EXIF:')
# print_exif_data(image_pil.getexif())
# print('Secondary EXIF:')
# print_exif_data(image_pil._getexif())


import exifread

# Open image file for reading (must be in binary mode)
with open("IMG_9163.jpg", "rb") as file_handle:
    # Return Exif tags
    tags = exifread.process_file(file_handle)
    geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print(f'{tag:40} |   {tags[tag]}')
    print(f'{"GPS Parsed DD Latitude":40} |   {dms_coordinates_to_dd_coordinates(tags["GPS GPSLatitude"].values, tags["GPS GPSLatitudeRef"])}')
    print(f'{"GPS Parsed DD Longitude":40} |   {dms_coordinates_to_dd_coordinates(tags["GPS GPSLongitude"].values, tags["GPS GPSLongitudeRef"])}')



# # iterating over all EXIF data fields
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes
#     if isinstance(data, bytes):
#         data = data.decode()
#     print(f"{tag:25}: {data}")

# u.debug_image_pil(image_pil)
# image_pil = u.rotate_image_according_to_exif_orientation(image_pil)
# u.debug_image_pil(image_pil)