#!/usr/bin/python3
import json
import os
""" file storage """


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, 'r') as f:
            objects_dict = json.load(f)

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        for obj_id, obj_data in objects_dict.items():
            class_name = obj_data['__class__']
            if class_name in classes:
                self.__objects[obj_id] = classes[class_name](**obj_data)
