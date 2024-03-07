import json
import os

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, 'r') as f:
            objects_dict = json.load(f)
        
        from models.base_model import BaseModel
        for obj_id, obj_data in objects_dict.items():
            class_name = obj_data['__class__']
