import os

class Separator(object):

    def __init__(self, configuration):
        self.configuration = configuration

    def separate(self):
        root_path = ""
        dir_list = []
        file_list = []
        tmp_list = []

        for title, items in self.configuration.items():
            if title == "root_path":
                root_path = items
                continue
            else:
                self.extract(title, items, dir_list, file_list, tmp_list)
        
        return root_path, dir_list, file_list

    def extract(self, title, items, dir_list, file_list, tmp_list):
        tmp_list.append(title)
        if type(items) == dict:
            self._dict_search(title, items, dir_list, file_list, tmp_list)
        else:
            self._other_search(title, items, dir_list, file_list, tmp_list)
        tmp_list.pop()

    def _dict_search(self, title, items, dir_list, file_list, tmp_list):
        
        if items == {}:
            dir_path = "/".join(tmp_list[0:-1])
            dir_list.append(os.path.join(dir_path, title))

        for sub_title, sub_items in items.items():
            self.extract(sub_title, sub_items, dir_list, file_list, tmp_list)


    def _other_search(self, title, items, dir_list, file_list, tmp_list):
        dir_path = "/".join(tmp_list[0:-1])
        
        if title != "file":
            return False
        if type(items) != list:
            return
        if dir_path in dir_list:
            return

        dir_list.append(dir_path)

        [file_list.append(os.path.join(dir_path, item)) for item in items]
