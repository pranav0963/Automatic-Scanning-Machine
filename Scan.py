import os


class PdfFile:
    def __init__(self, name):
        self.path = f'docs/{name}'

    def save(self, list, image):
        if not os.path.exists('docs/'):
            os.mkdir("docs/")
            f = open(self.path, "wb")
            f.close()

        list[0].save(self.path, save_all=True, append_images=list[1:])
