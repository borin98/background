# Background change for linux distros

This repository contains a python code that changes the background given a time and the directory with the wallpapers

**OBS** : This repo only works for __.png__ and __.jpg__ files

## Pre-requisites

__pyton 3.9 or above__

## Usage

To try this code, run

```sh
python3 background.py -t time_minutes -p directory_path
```
Where :

__time_minutes__ is the time in minutes to change the wallpapers

__directory_path__ is the path directory that contains all the wallpapers

### Example run

Let's see an example on how you can run this code

```sh
python3 background.py -t 30 -p /home/usr/Documents/Wallpapers/
```

In this case, __every file in "/home/usr/Documents/Wallpapers/" will be a wallpaper every 30 minutes__

## TODO

- Creating a loading screen to show how much time left to change to the next wallpaper
- Creating more warning and log to user
- Need to change all print to log
- Need to place a flag if the user wants cicle or not the wallpapers

## Special Thanks

Also, thanks to [MaTyson](https://github.com/MaTyson) to make the core of this script !!