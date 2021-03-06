# SaturdayShortcuts

This is a collection of python scripts, that simplifies repetative Tasks on Ubuntu with **Autokey**. 
An installation guide for Autokey is [here.](https://github.com/autokey/autokey/wiki/Installing#debian-and-derivatives)

## How to use the scripts:
1. Open Autokey and go to "new script".
2. Copy and paste the script.
3. Define your prefered key, which will trigger the script.

## To go to the youtube channel, click the image:
[![SaturdayShortcuts-youtube channel](brand_git.png)](https://www.youtube.com/channel/UCSIoiszi1R4sgS9CEme7R8A)


---
**#Episode01:** *Translate selected text into another language*

```python
text = clipboard.get_selection()
url = "firefox -new-tab 'https://www.linguee.de/deutsch-englisch/search?source=auto&query=" + text + "'"
output = system.exec_command(url)
```
---

**#Episode02:** *Automatic unpacking zip files in the Download folder*

```python
import os, zipfile
import subprocess
dir_name = '/home/jan-hendrik/Downloads/'
extension = ".zip"
os.chdir(dir_name) # change directory from working dir to dir with files
for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name + item[:-4]) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
        subprocess.Popen(['xdg-open', dir_name + item[:-4] + '/']) #open folder
```
**#Episode03:** *Automation of screenshots*

```python
working_directory= "~/Downloads/"
time.sleep(0.1) # without this, the command does not work 

command = "gnome-screenshot -a  -f '/tmp/temp.png' "
output = system.exec_command(command)

name = dialog.input_dialog(title='Enter a value', message='Enter a value', default='').data


from_path = '/tmp/temp.png'
to_path   = working_directory + name + '.png'

command2 = "mv " + from_path + " " + to_path 

system.exec_command(command2)
dialog.info_dialog( title='Information', message='Screenshot moved to ' + to_path  )
```
