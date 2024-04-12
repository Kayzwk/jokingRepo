import time
import sys

def load_wallpaper():
    bar_width = 50
    print("Loading wallpaper...")
    for i in range(bar_width + 1):
        sys.stdout.write('\r')
        sys.stdout.write("[%-{}s] %d%%".format(bar_width) % ('=' * i, i * 100 / bar_width))
        sys.stdout.flush()
        time.sleep(0.1)  
    print("\nWallpaper loaded successfully!")

load_wallpaper()

