import time
import requests
import vk
import os.path
import json
import yandex
from tqdm import tqdm
from pprint import pprint

vk_token = ''
token_yandex = ''
#folder = 'photos/'
user_info = 'i_sugak'
#id_user = input('Введите id пользователя VK:')
#token_yandex = input('Введите токен с Полигона Яндекс.Диска:')
folder = input('Введите название папки для фотографий:')


def save_photo(directory, photos_profile, count=5):
    numb = 0
    #for photo in tqdm(photos_profile, desc='Скачивание фотографий на диск', colour='green', total=count, ncols=150):
    for photo in photos_profile:
        if numb < count:
            sizes = photo['sizes']
            big_size = vk_info.big_size(sizes)
            dict_photos = {'likes': photo['likes']['count'],
                           'date': photo['date'],
                           'url': big_size['url'],
                           'type': big_size['type']}
            response = requests.get(dict_photos['url'])
            if response.status_code == 200:
                filename = str(dict_photos['likes'])
                file_path = directory + filename
                filename_jpg = filename + ".jpg"
                print(filename_jpg, big_size['url'])
                #yandex.upload_dir_files(big_size['url'], token_yandex)
                date_photo = str(time.strftime("%Y%m%d", time.gmtime(dict_photos['date'])))
                upload_name = disk.upload(big_size['url'], folder + '/' + filename, date_photo, dict_photos['type'])
                # with open('result.json', 'w') as f:
                #     file_json = [{
                #         "file_name": filename + '.jpg',
                #         "size": dict_photos['type']
                #     }]
                #     json.dump(file_json, f)


            # if os.path.exists(os.path.abspath(directory + str(dict_photos['likes']) + ".jpg")):
            #     if response.status_code == 200:
            #         filename = str(dict_photos['likes']) + '_' \
            #                    + str(time.strftime("%Y%m%d", time.gmtime(dict_photos['date'])))
            #         file_path = directory + filename
            #         filename_jpg = file_path + ".jpg"
            #         filename_json = file_path + ".json"
            #         with open(filename_jpg, 'wb') as f:
            #             f.write(response.content)
            #         with open(filename_json, 'w') as f:
            #             file_json = [{
            #                 "file_name": filename + '.jpg',
            #                 "size": dict_photos['type']
            #             }]
            #             json.dump(file_json, f)
            # else:
            #     if response.status_code == 200:
            #         filename = str(dict_photos['likes'])
            #         file_path = directory + filename
            #         filename_jpg = file_path + ".jpg"
            #         filename_json = file_path + ".json"
            #         with open(filename_jpg, 'wb') as f:
            #             f.write(response.content)
            #         with open(filename_json, 'w') as f:
            #             file_json =[{
            #                 "file_name": filename + '.jpg',
            #                 "size": dict_photos['type']
            #             }]
            #             json.dump(file_json, f)
            numb += 1
    return


if __name__ == '__main__':
    disk = yandex.YaUploader(token_yandex)
    disk.check_folder(folder)
    vk_info = vk.vkGet(vk_token, '5.131')
    user_id = vk_info.get_users(user_info)
    photos_prof = vk_info.photos_get(user_id)
    count_photo = photos_prof['count']
    pprint(f"Найдено {count_photo} фотографий")
    count_photos = int(input('Введите введите количество скачиваемых фотографий:'))
    save_photo(folder, photos_prof['items'],  count_photos)
    #print(disk.upload('https://sun9-85.userapi.com/c10954/u3415629/-6/z_b7c291aa.jpg', 'VK/VK.jpg'))
    #print('Получить ссылку', disk.get_upload_link(folder))
    #check = disk.check_folder(folder)
    #yandex.upload_dir_files(folder, token_yandex)
    #print(check)