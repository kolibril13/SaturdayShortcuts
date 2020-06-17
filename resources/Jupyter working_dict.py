with open('/home/jan-hendrik/Desktop/physics_working_directory.txt') as f:
    data = f.readlines()
working_directory = data[0]
my_directory = working_directory[:-2]

a = """ gnome-terminal"""
b = f""" --working-directory={my_directory} """
c = """ -e '/home/jan-hendrik/anaconda3/bin/jupyter-notebook' """
system.exec_command(a + b + c)
