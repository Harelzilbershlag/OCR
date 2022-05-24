import os

class Txt:
    def __init__(self):
        pass


    def wrtie(self, file_name, text, path_out):
        text_result = open(os.path.join(path_out, file_name + ".txt"), "wb")
        text_result.write(text.encode('UTF-8'))
        text_result.close()
