# SaturdayShortcuts

This is a collection of python scripts, that simplifies repetative Tasks on Ubuntu with **Autokey**. 
An installation guide for Autokey is [here.](https://github.com/autokey/autokey/wiki/Installing#debian-and-derivatives)

## How to use the scripts:
1. Open Autokey and go to "new script".
2. Copy and paste the script.
3. Define your prefered key, which will trigger the script.

---
**#Episode01:** *Translate selected text into another language*

```python
text = clipboard.get_selection()
url = "firefox -new-tab 'https://www.linguee.de/deutsch-englisch/search?source=auto&query=" + text + "'"
output = system.exec_command(url)
```
---
