#!/usr/bin/env python3

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter."""
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Displays the help documentation for 'quit' command."""
        print("Quit command to exit the program.")

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print()
        return True

    def help_EOF(self):
        """Displays the help documentation for 'EOF' command."""
        print("EOF command to exit the program. Use Ctrl+D.")

    def do_create(self, class_name):
        """Creates a new instance of BaseModel and prints the id."""
        if not class_name:
            print("** class name missing **")
            return
        if class_name in self.classes:
            instance = self.classes[class_name]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """ Help documentation for create command. """
        print("Creates a new instance of BaseModel and prints the id.")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def help_show(self):
        """ Help docummentation for show command """
        print("Prints the string representation of an instance.")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """ Help docummentation for destroy command """
        print("Deletes an instance based on the class name and id.")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        all_objects = storage.all()
        result = []
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objects.items():
                if key.startswith(arg):
                    result.append(str(obj))
        else:
            for obj in all_objects.values():
                result.append(str(obj))
        print(result)

    def help_all(self):
        """ Help docummentation for all command """
        print("Prints all string representation of all instances.")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 4:
            print("** value missing **" if len(args) < 3
                  else "** attribute name missing **" if len(args) < 2
                  else "** instance id missing **" if len(args) < 1
                  else "** class name missing **")
            return
        class_name, instance_id, att_name, att_value = (
            args[0], args[1], args[2], args[3].strip('"')
        )
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in all_objects:
            setattr(all_objects[key], att_name, att_value)
            all_objects[key].save()
        else:
            print("** no instance found **")

    def help_update(self):
        """ Help documentaton for update command """
        print("Updates an instance based on the class name and id.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
