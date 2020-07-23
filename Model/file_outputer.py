import os
import pathlib

from Model.outputer import Outputer

class FileOutputer(Outputer):

    def __init__(self, root_path, file_list):
        self.root_path = root_path
        self.file_list = file_list

    def output(self):
        for file_name in self.file_list:
            merged_path = os.path.join(self.root_path, file_name)
            file_path = pathlib.Path(merged_path)
            file_path.touch()
            print(file_path)