from PyQt5.QtWidgets import *
import codecs


def file_open_return_helper(self):
    # getting path and bool value
    path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

    # if path is true
    if path:
        # try opening path
        try:
            with codecs.open(path, "r", "utf-8") as f:
                # read the file
                text = f.read()

        # if some error occurred
        except Exception as e:
            pass
        # else
        else:
            return text, path