import requests
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path, date_photo):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path + ".jpg", 'overwrite': 'false'}
        response = requests.get(upload_url, headers=headers, params=params)
        print(disk_file_path)
        print(response.status_code)
        if response.status_code == 200:
            return response.json
        else:
            filename = disk_file_path + date_photo + ".jpg"
            params = {'path': filename, 'overwrite': 'false'}
            response = requests.get(upload_url, headers=headers, params=params)
            print('Уже есть такая фотография', filename)
            return response.json

    def upload(self, file_path: str, disk_file_path, date_photo, sizes):

        href = self.get_upload_link(disk_file_path=disk_file_path, date_photo=date_photo).get('href', '')
        with requests.get(file_path, stream=True) as r:
            response = requests.put(href, data=r.content)
            response.raise_for_status()
        with open('result.json', 'w') as f:
            file_json = [{
                "file_name": disk_file_path + '.jpg',
                "size": sizes
            }]
            json.dump(file_json, f)
        return

    def check_folder(self, check_folder):
        url_check = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': check_folder}
        headers = self.get_headers()
        response = requests.put(url_check, headers=headers, params=params)
        return


def upload_dir_files(dir_to_file, token):
    only_files = dir_to_file
    #only_files = [f for f in listdir(dir_to_file) if isfile(join(dir_to_file, f))]
    print(only_files)
    #for files in tqdm(only_files, desc='Загрузка фотографий и json файлов на Яндекс.Диск', colour='green', ncols=150):
    for files in only_files:
        path_to_file = dir_to_file + files
        filename = os.path.basename(path_to_file)
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file, dir_to_file + filename)
        #os.remove(path_to_file)
    return


# token_yandex = ''
# path_to_file = 'requirements.txt'
# filename = os.path.basename(path_to_file)
# print(filename)
# disk = YaUploader(token_yandex)
# disk.check_folder('VK')
# print(disk.upload('https://sun9-85.userapi.com/c10954/u3415629/-6/z_b7c291aa.jpg', 'VK/VK.jpg'))
