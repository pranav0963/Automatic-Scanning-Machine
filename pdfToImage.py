from pdf2image import convert_from_path


def convert(file):
    pages = convert_from_path(file, 500)
    i = 0
    for page in pages:
        page.save(f'image{i}.jpg', "JPEG")
        i += 1
