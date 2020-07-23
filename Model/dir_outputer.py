import os
import pathlib

from Model.outputer import Outputer

class DirOutputer(Outputer):

    def __init__(self, root_path, dir_list):
        self.root_path = root_path
        self.dir_list = dir_list
    
    def output(self):
        for dir_name in self.dir_list:
            merged_path = os.path.join(self.root_path, dir_name)
            dir_path = pathlib.Path(merged_path)
            
            # ディレクトリ作成
            self._make_dir(dir_path)            
            
    def _make_dir(self, dir_path):
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            print(dir_path)
