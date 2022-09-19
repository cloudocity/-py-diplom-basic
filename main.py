import time
import requests
import vk
import yandex
from tqdm import tqdm
from pprint import pprint
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")


vk_token = config["VK"]["vk_token"]
token_yandex = config["yandex"]["yandex_token"]
user_info = 'i_sugak'
folder = input('Введите название папки для фотографий:')


def save_photo(directory, photos_profile, count=5):
    numb = 0
    for photo in tqdm(photos_profile, desc='Выгрузка фото профиля на ЯндексДиск', colour='green', total=count, ncols=150):
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
                date_photo = str(time.strftime("%Y%m%d", time.gmtime(dict_photos['date'])))
                upload_name = disk.upload(big_size['url'], folder + '/' + filename, date_photo, dict_photos['type'])
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
    print('Выгрузка закончена информацию можно посмотреть в result.json')