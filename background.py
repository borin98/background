import numpy
import requests
import os
import argparse
import time
from dotenv import load_dotenv


class Wallpaper:
    def __init__(self):
        pass

    @staticmethod
    def get_earthview():
        img_json_url = "https://raw.githubusercontent.com/limhenry/earthview/master/earthview.json"
        req = requests.get(img_json_url)
        json_list = req.json()
        img_json = numpy.random.choice(json_list)

        wallpaper_url = img_json['image']
        wallpaper = requests.get(wallpaper_url)

        with open('tmp.jpg', 'wb') as f:
            f.write(wallpaper.content)

    @staticmethod
    def get_pexels():
        load_dotenv()
        token = os.getenv('PEXELS_TOKEN')
        payload = {'Authorization': token}

        query = [
            'flower',
            'colors',
            'animals',
            'dogs',
            'cats',
            'birds'
            'sky',
            'galaxy',
            'food',
            'pasta',
            'noodle',
            'sea',
            'land',
            'rainbow',
            'night',
            'beach',
            'drinks',
            'bees',
            'icelands',
            'nature',
            'rain',
            'music',
            'mushroom',
            'bread',
            'waterfall',
            'greek',
            'rome',
            'elephant'
        ]

        lucky = numpy.random.randint(1, 99)
        url = 'https://api.pexels.com/v1/search?per_page=1&page=' + str(lucky) + '&query=' + numpy.random.choice(query)

        res = requests.get(url, headers=payload)
        if res.status_code == 200:
            img_url = ''
            try:
                img_url = res.json().get('photos')[0]['src']['original']
            except:
                print('oops')
            else:
                img = requests.get(img_url)
                with open('tmp.jpg', 'wb') as f:
                    f.write(img.content)
        else:
            print('Http request failed')

    @staticmethod
    def set_wallpaper():
        # self.get_earthview()
        Wallpaper.get_pexels()
        path = os.getcwd() + '/tmp.jpg'

        cmd = "gsettings set org.gnome.desktop.background picture-uri file:" + path
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
