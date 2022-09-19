import requests
import os
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path, date_photo, sizes):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path + ".jpg", 'overwrite': 'false'}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 200:
            file_json = [{
                "file_name": disk_file_path,
                "size": sizes
            }]
            with open('result.json', 'a', encoding='utf-8') as file:
                json.dump(file_json, file)
                file.write('\n')
            return response.json()
        else:
            filename = disk_file_path + date_photo + ".jpg"
            file_json = [{
                "file_name": filename,
                "size": sizes
            }]
            params = {'path': filename, 'overwrite': 'true'}
            response = requests.get(upload_url, headers=headers, params=params)
            with open('result.json', 'a', encoding='utf-8') as file:
                json.dump(file_json, file)
                file.write('\n')
            return response.json()

    def upload(self, file_path: str, disk_file_path, date_photo, sizes):
        href = self.get_upload_link(disk_file_path=disk_file_path, date_photo=date_photo, sizes=sizes).get('href', '')
        with requests.get(file_path, stream=True) as r:
            response = requests.put(href, data=r.content)
            response.raise_for_status()
        return

    def check_folder(self, check_folder):
        url_check = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': check_folder}
        headers = self.get_headers()
        response = requests.put(url_check, headers=headers, params=params)
        return


def upload_dir_files(dir_to_file, token):
    only_files = dir_to_file
    for files in only_files:
        path_to_file = dir_to_file + files
        filename = os.path.basename(path_to_file)
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file, dir_to_file + filename)
    return

