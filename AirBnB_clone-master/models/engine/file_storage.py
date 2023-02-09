"""
Class FileStorage that serializes instances 
to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage():
    """
    class FileStorage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json_obj = {}
            for key, value in FileStorage.__objects.items():
                json_obj[key] = value.to_dict()
            print(json_obj)
            json.dump(json_obj, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="UTF-8") as f:
                json_obj = json.load(f)
                for key, value in json_obj.items():
                    class_name = value["__class__"]
                    value.pop("__class__")
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    