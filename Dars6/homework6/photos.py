# 'https://randomuser.me/api'

import os
from threading import Thread

import httpx
import requests


def thumb_photos():
    folder_path = "thumb_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1,100):
        image_url = f"https://randomuser.me/api/portraits/thumb/men/{i}.jpg"
        image_filename = f"{folder_path}/thumbnails_{i}.jpg"

        try:
            response = httpx.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} image saved")
        except httpx.exceptions.RequestException as e:
            print(f"{i} Cannot download image. Error: {e}")

    print("All images downloaded")

def medium_photos():
    folder_path = "medium_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1,100):
        image_url = f"https://randomuser.me/api/portraits/med/men/{i}.jpg"
        image_filename = f"{folder_path}/medium_{i}.jpg"

        try:
            response = httpx.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} image saved")
        except httpx.exceptions.RequestException as e:
            print(f"{i} Cannot download image. Error: {e}")

    print("All images downloaded")

def large_photos():
    folder_path = "large_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1,100):
        image_url = f"https://randomuser.me/api/portraits/men/{i}.jpg"
        image_filename = f"{folder_path}/large_{i}.jpg"

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} image saved")
        except requests.exceptions.RequestException as e:
            print(f"{i} Cannot download image. Error: {e}")

    print("All images downloaded")

if __name__ == '__main__':
    threads = []
    for func in [thumb_photos, medium_photos, large_photos]:
        t = Thread(target=func)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print("All images downloaded")