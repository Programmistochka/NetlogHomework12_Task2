import requests
import os

class YaUploader:
    
    base_host = "https://cloud-api.yandex.net:443"
    
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        """Метод для передачи заголовков"""
        return {
            'Content_Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers = self.get_headers(), params = params)
        print(response.status_code)
        return response.json()['href']
    
    def upload(self, file_path: str, yandex_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers = self.get_headers())
        if response.status_code == 201:
            print('Загрузка прошла успешно')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = input('Введите Token: ')
    path_to_file = input('Введите путь к файлу: ')
    file_name = input('Введите имя файла: ')
    full_path = os.path.join(path_to_file, file_name)
    print(full_path)
    uploader = YaUploader(token)
    uploader.upload(full_path, f'/{file_name}')
