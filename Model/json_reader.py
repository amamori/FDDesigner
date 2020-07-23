
import json

class JsonReader(object):

    def __init__(self, specification_path):
        self.specification_path = specification_path
        self.json_reader = None
    
    def __enter__(self):
        self.json_reader = open(self.specification_path, mode="r")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.json_reader.close()
    
    def get_configuration(self):
        return json.load(self.json_reader)