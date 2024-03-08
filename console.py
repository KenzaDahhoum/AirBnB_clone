#!/usr/bin/env python3
from models.base_model import BaseModel
from models import storage
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = ' (hbnb) '
    classes = {"BaseModel": BaseModel}
    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print the help documentation for 'quit' command."""
        print("Quit command to exit the program.")

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print()
        return True

    def help_EOF(self):
        """Print the help documentation for 'EOF' command."""
        print("EOF command to exit the program. Use Ctrl+D.")


    
    def do_create(self, class_name):
        if not class_name:
            print("** class name missing **")
            return

        if class_name in self.classes:
            instance = self.classes[class_name]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")



    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in self.classes:
            print ("** class doesn't exist **")
            return

        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"

        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")



    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in self.classes:
            print ("** class doesn't exist **")
            return

        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"

        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")



    def do_all(self, arg):
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



    def do_update(self, arg):
        args = arg.split()
        if len(args) < 4:
            print("** value missing **" if len(args) < 3 else "** attribute name missing **" if len(args) < 2 else "** instance id missing **" if len(args) < 1 else "** class name missing **")
            return

        class_name, instance_id, att_name, att_value = args[0], args[1], args[2], args[3].strip('"')

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
