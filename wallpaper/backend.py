import time
import os
import random


def change_wallpaper():
    # Replace the file path with the path to the folder containing
    #  your wallpapers
    path = "/home/wethinkcode/Pictures/Wallpapers"
    wallpapers = os.listdir(path)
    # Replace the file extension with the extension of your wallpaper files
    wallpapers = [wallpaper for wallpaper in wallpapers if wallpaper.endswith(".jpg")]
    # Shuffle the list of wallpapers
    random.shuffle(wallpapers)
    # Set the index of the wallpaper you want to use first
    index = 0
    while True:
        # Set the file path to the next wallpaper in the list
        wallpaper_path = os.path.join(path, wallpapers[index])
        # Set the command to change the wallpaper
        command = "gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path
        os.system(command)
        # Wait for 5 minutes
        time.sleep(300)
        # Increment the index to use the next wallpaper in the list, 
        # looping back to the beginning if necessary
        index = (index + 1) % len(wallpapers)

if __name__ == "__main__":
    change_wallpaper()
