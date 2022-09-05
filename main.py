import time
import requests
import vk
import os.path
import json
import yandex

vk_token = ''
token_yandex = ''
folder = 'photos/'


def save_photo(directory, photos_profile, count=5):
    numb = 0
    for photo in photos_profile:
        if numb < count:
            sizes = photo['sizes']
            big_size = photos.big_size(sizes)
            dict_photos = {'likes': photo['likes']['count'],
                           'date': photo['date'],
                           'url': big_size['url'],
                           'type': big_size['type']}
            response = requests.get(dict_photos['url'])
            if os.path.exists(os.path.abspath(directory + str(dict_photos['likes']) + ".jpg")):
                if response.status_code == 200:
                    filename = str(dict_photos['likes']) + '_' \
                               + str(time.strftime("%Y%m%d", time.gmtime(dict_photos['date'])))
                    file_path = directory + filename
                    filename_jpg = file_path + ".jpg"
                    filename_json = file_path + ".json"
                    with open(filename_jpg, 'wb') as f:
                        f.write(response.content)
                    with open(filename_json, 'w') as f:
                        file_json = [{
                            "file_name": filename + '.jpg',
                            "size": dict_photos['type']
                        }]
                        json.dump(file_json, f)
            else:
                if response.status_code == 200:
                    filename = str(dict_photos['likes'])
                    file_path = directory + filename
                    filename_jpg = file_path + ".jpg"
                    filename_json = file_path + ".json"
                    with open(filename_jpg, 'wb') as f:
                        f.write(response.content)
                    with open(filename_json, 'w') as f:
                        file_json =[{
                            "file_name": filename + '.jpg',
                            "size": dict_photos['type']
                        }]
                        json.dump(file_json, f)
            numb += 1
    return


if __name__ == '__main__':
    photos = vk.vkGet(vk_token, '5.131')
    photos_prof = photos.photos_get(3415629)
    save_photo(folder, photos_prof)
    yandex.upload_dir_files(folder, token_yandex)
