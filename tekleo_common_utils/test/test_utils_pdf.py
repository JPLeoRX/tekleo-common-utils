# Run dependency injections
from injectable import load_injection_container
load_injection_container('../')
from tekleo_common_utils.utils_file import UtilsFile
from tekleo_common_utils.utils_pdf import UtilsPdf
utils_file = UtilsFile()
utils_pdf = UtilsPdf()

pdf_file_path = "Assessment_of_antifungal_activity_of_ProRoot_miner.pdf"

# Conversion to text
pages = utils_pdf.convert_to_texts(pdf_file_path)
assert len(pages) == 6

# Conversion to images
pdf_page_image_paths = utils_pdf.convert_to_images(pdf_file_path, "/Users/leo/tekleo/tekleo-common-utils/tekleo_common_utils/test/pdf_output", thread_count=8, output_image_format="jpg")
assert len(pdf_page_image_paths) == 6
for p in pdf_page_image_paths:
    print(p)
print("----------")

# Open file
pdf_bytes = utils_file.open_file_to_bytes(pdf_file_path)

# Get number of pages
number_of_pages = utils_pdf.get_number_of_pages_from_bytes(pdf_bytes)
assert number_of_pages == 6

# Render all pages
pdf_page_image_paths = utils_pdf.render_from_bytes_to_image_paths_all_pages(pdf_bytes, thread_count=8)
assert len(pdf_page_image_paths) == number_of_pages
for p in pdf_page_image_paths:
    print(p)
print("----------")

# Render only 3 pages
pdf_page_image_paths = utils_pdf.render_from_bytes_to_image_paths(pdf_bytes, 2, 4, thread_count=8)
assert len(pdf_page_image_paths) == 3
for p in pdf_page_image_paths:
    print(p)
print("----------")

# Render only 1 page
pdf_page_image_path = utils_pdf.render_from_bytes_to_image_paths_single_page(pdf_bytes, 5)
print(pdf_page_image_path)

# Render all pages as JPG
pdf_page_image_paths = utils_pdf.render_from_bytes_to_image_paths_all_pages(pdf_bytes, thread_count=8, output_image_format="jpg")
assert len(pdf_page_image_paths) == number_of_pages
for p in pdf_page_image_paths:
    print(p)
print("----------")
