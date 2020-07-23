import os

from Model.json_reader import JsonReader
from Model.separator import Separator
from Model.dir_outputer import DirOutputer
from Model.file_outputer import FileOutputer


def make_file_and_directry_from_specification(specification_path):
    
    # Jsonパーサー
    with JsonReader(specification_path) as jr:
        configuration = jr.get_configuration()

    # 分別
    root_path, dir_list, file_list = Separator(configuration).separate()

    # ディレクトリ、ファイル出力
    outputer_list = [DirOutputer(root_path, dir_list), FileOutputer(root_path, file_list)]
    for outputer in outputer_list:
        outputer.output()