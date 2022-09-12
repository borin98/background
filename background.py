import argparse
import os
import time
import glob
import random


class Wallpaper(object):
    def __init__(self, wallpaper_path: str):
        self._wallpaper_path = wallpaper_path
        self._wallpaper_list = glob.glob(wallpaper_path + "*.jpg") + glob.glob(wallpaper_path + "*.png")
        self._wallpaper_list_copy = self._wallpaper_list.copy()
        self._wallpaper_list_len = len(self._wallpaper_list)

    def _remove_wallpaper_element(self, wallpaper_to_remove: str):
        self._wallpaper_list.remove(wallpaper_to_remove)
        self._wallpaper_list_len -= 1

    @staticmethod
    def _set_wallpaper(wallpaper_list: list[str]) -> str:
        secure_random = random.SystemRandom()
        path_img = secure_random.choice(wallpaper_list)
        print(len(path_img) * "=")
        print("{} was chosen as wallpaper".format(path_img.split("/")[-1]))
        print(len(path_img) * "=")
        cmd = "gsettings set org.gnome.desktop.background picture-uri-dark file://" + path_img
        os.system(cmd)
        return path_img

    def run_wallpaper(self):
        chosen_wallpaper = self._set_wallpaper(self._wallpaper_list)
        self._remove_wallpaper_element(chosen_wallpaper)

        if (not self._wallpaper_list):
            self._wallpaper_list = self._wallpaper_list_copy.copy()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help='Enter time in minutes')
    parser.add_argument('-p', '--path', help="Enter the path to wallpapers")

    args = parser.parse_args()
    minutes = int(args.time)
    files_path = args.path
    wallpaper = Wallpaper(files_path)
    while True:
        wallpaper.run_wallpaper()
        time.sleep(minutes * 60)


if __name__ == '__main__':
    main()
