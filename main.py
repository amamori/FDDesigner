import json
import os

import Controller.conversation


specification_file_name = "specification.json"

def main():
    # フォルダ構成設計書のパス
    specification_path = os.path.join(os.path.dirname(__file__), specification_file_name)
    Controller.conversation.make_file_and_directry_from_specification(specification_path)

if __name__ == "__main__":
    main()