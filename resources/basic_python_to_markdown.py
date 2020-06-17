text = clipboard.get_clipboard()
new_text = "```python \n" + text + "\n```"
keyboard.send_keys(new_text)
