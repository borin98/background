import argparse
import os
import time
import glob
import random
class Wallpaper:
    def __init__(self):
        pass

    @staticmethod
    def set_wallpaper():
        # self.get_earthview()
        path_vec = glob.glob("/home/gabriel_macedo/Documents/Wallpapers/*.jpg") + glob.glob("/home/gabriel_macedo/Documents/Wallpapers/*.png")
        secure_random = random.SystemRandom()
        path_img = secure_random.choice(path_vec)
        cmd = "gsettings set org.gnome.desktop.background picture-uri-dark file://" + path_img
        os.system(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help='Enter time in minutes')

    args = parser.parse_args()
    minutes = int(args.time)
    while True:
        Wallpaper.set_wallpaper()
        time.sleep(minutes * 60)


if __name__ == '__main__':
    main()
