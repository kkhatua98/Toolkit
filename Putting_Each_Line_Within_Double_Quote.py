import winclip32
import os
import io

buf = io.StringIO(winclip32.get_clipboard_data(winclip32.UNICODE_STD_TEXT))

while True:
    a = buf.readline()
    if not a:
        break
    print(f'"{a[:-1]}",')
