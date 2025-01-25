import os
from scripts.file_system_operations import TMP_DIR
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DownloadFiles:

    def checking_download_file(self):

        if not os.path.exists(TMP_DIR):
            logging.error(f"Директория {TMP_DIR} не существует.")
            raise FileNotFoundError(f"Директория {TMP_DIR} не существует.")

        files = os.listdir(TMP_DIR)
        if len(files) == 0:
            logging.error('Нет папки, либо папка пуста!')
            raise FileNotFoundError('Нет папки, либо папка пуста!')

        for file in files:
            file_xlsx = os.path.join(TMP_DIR, file)
            if not os.path.isfile(file_xlsx):
                logging.error(f"Файл {file} не найден или это не файл.")
                raise FileNotFoundError(f"Файл {file} не найден или это не файл.")

            file_size = os.path.getsize(file_xlsx)
            if file_size == 0:
                logging.error(f"Файл {file} пустой.")
                raise ValueError(f"Файл {file} пустой.")

            logging.info(f'Файл {file} существует и содержит информацию.')

    def delete_file(self):
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)
