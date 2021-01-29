from PIL import Image  # Will need to make sure PIL is installed
import mss

with mss.mss() as mss_instance:
    monitor_1 = mss_instance.monitors[2]
    screenshot = mss_instance.grab(monitor_1)

    img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
    img.show()  # Show the image using the default image viewer
