
def write(content, document):
    paragraph = document.add_paragraph(str(ascii(content)))
    paragraph_format = paragraph.paragraph_format
    paragraph_format.page_break_before = True
    return document

