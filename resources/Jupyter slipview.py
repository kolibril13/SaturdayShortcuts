my_directory = "/home/jan-hendrik/python/projects/jupyter-splitview"

a = """ gnome-terminal"""
b = f""" --working-directory={my_directory} """
c = """ -e '/home/jan-hendrik/anaconda3/bin/jupyter-notebook' """
system.exec_command(a + b + c)
