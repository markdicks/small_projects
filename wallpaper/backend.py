import os
import random
import time

# Specify the directory containing your wallpaper images
wallpaper_dir = '/path/to/wallpapers'

# Define a function to change the wallpaper
def change_wallpaper():
    # Get a list of all the files in the wallpaper directory
    wallpaper_list = [os.path.join(wallpaper_dir, f) for f in os.listdir(wallpaper_dir) if os.path.isfile(os.path.join(wallpaper_dir, f))]

    # Filter out any non-image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    wallpaper_list = [f for f in wallpaper_list if os.path.splitext(f)[1].lower() in image_extensions]

    # Choose a random wallpaper from the list
    wallpaper = random.choice(wallpaper_list)

    # Set the wallpaper using the appropriate command for your desktop environment
    os_name = os.name
    if os_name == 'posix':
        # For Linux
        desktop_environment = os.environ.get('DESKTOP_SESSION')
        if desktop_environment == 'gnome':
            os.system('gsettings set org.gnome.desktop.background picture-uri "file://%s"' % wallpaper)
        elif desktop_environment == 'mate':
            os.system('mateconftool-2 -t string -s /desktop/mate/background/picture_filename "%s"' % wallpaper)
        elif desktop_environment == 'xfce':
            os.system('xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s "%s"' % wallpaper)
        else:
            print('Unsupported desktop environment')
    elif os_name == 'nt':
        # For Windows
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)
    else:
        print('Unsupported operating system')

# Set the wallpaper every 5 minutes
while True:
    change_wallpaper()
    time.sleep(300)
