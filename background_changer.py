import ctypes
import requests
import time

def set_wallpaper(url):
    response = requests.get(url)
    path = '' #The path that you want the image to be saved
    with open(path, 'wb') as f:
        f.write(response.content)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def get_random_image():
    access_key = '' #Your API access key on unsplash
    url = f'https://api.unsplash.com/photos/random?client_id={access_key}'
    response = requests.get(url)
    data = response.json()
    return data['urls']['full']

if __name__ == '__main__':
    while True:
        url = get_random_image()
        set_wallpaper(url)
        print('done!')
        time.sleep(60*60*12) #The time that you want the image to be changed(It is set to 12 hours for each photo)