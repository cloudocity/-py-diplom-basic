import requests
import os
from os import listdir
from os.path import isfile, join


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, disk_file_path):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return


def upload_dir_files(dir_to_file, token):
    only_files = [f for f in listdir(dir_to_file) if isfile(join(dir_to_file, f))]
    for files in only_files:
        path_to_file = 'photos/' + files
        filename = os.path.basename(path_to_file)
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file, 'vk_photo/' + filename)
        os.remove(path_to_file)
    return