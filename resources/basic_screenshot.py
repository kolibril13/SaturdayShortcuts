import time
import os

working_directory = "~/Downloads/"
time.sleep(0.1)  # without this, the command does not work

command = "gnome-screenshot -a  -f '/tmp/temp.png' "
os.system(command)

name = dialog.input_dialog(title='', message='Screenshot name:', default='').data

from_path = '/tmp/temp.png'
to_path = working_directory + name + '.png'

command2 = "mv " + from_path + " " + to_path

os.system(command2)
