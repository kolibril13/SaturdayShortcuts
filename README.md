# SaturdayShortcuts

This is a collection of python scripts, that simplifies repetative Tasks on Ubuntu with **Autokey**. 
An installation guide for Autokey is [here.](https://github.com/autokey/autokey/wiki/Installing#debian-and-derivatives)

## How to use the scripts:
1. Open Autokey and go to "new script".
2. Copy and paste the script.
3. Define your prefered key, which will trigger the script.


# Click here to open the channel:
[![IMAGE ALT TEXT HERE](https://www.youtube.com/channel/UCSIoiszi1R4sgS9CEme7R8A
]
https://www.youtube.com/channel/UCSIoiszi1R4sgS9CEme7R8A

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
