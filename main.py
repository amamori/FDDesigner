import json
import os
import pathlib


specification_file_name = "specification.json"


def make_dir(new_dir_name):
    new_dir_path = os.path.join(os.path.dirname(__file__), new_dir_name)
    # pathlib.Path(new_dir_path).mkdir(parents=True, exist_ok=True)
    print(new_dir_path)

def make_file(new_file_name):
    new_file_path = os.path.join(os.path.dirname(__file__), new_file_name)
    # pathlib.Path(new_file_path).touch()
    print(new_file_path)

def make_files(new_files, dir_path):
    
    for new_file in new_files:
        new_file_path = os.path.join(os.path.dirname(__file__), dir_path, new_file)
        # pathlib.Path(new_file_path).touch()
        print(new_file_path)



def parse_dict(target_dict, stack_lists):
    for dir_name, value in target_dict.items():

        if dir_name == "file":
            dir_path_name = "/".join(stack_lists)    
            if type(value) is list:
                make_files(value, dir_path_name)
            elif type(value) is str:
                make_dir(dir_path_name)
                if len(value) > 0:
                    file_path = dir_path_name +"/"+ value
                    make_file(file_path)
            else:
                continue
        else:
            stack_lists.append(dir_name)
            dir_path_name = "/".join(stack_lists)

            if type(value) is list:
                make_files(value, dir_path_name)
            elif type(value) is str:
                make_dir(dir_path_name)
                if len(value) > 0:
                    file_path = dir_path_name +"/"+ value
                    make_file(file_path)
            else:
                make_dir(dir_path_name)
                if len(value) > 0:
                    parse_dict(value, stack_lists)        
            stack_lists.pop()

def main():
    # フォルダ構成設計書のパス
    specification_path = os.path.join(os.path.dirname(__file__), specification_file_name)

    # 設計書を展開
    with open(specification_path, mode="r") as j:
        dir_configuration = json.load(j)
    
    stack_lists = []
    parse_dict(dir_configuration, stack_lists)


if __name__ == "__main__":
    main()