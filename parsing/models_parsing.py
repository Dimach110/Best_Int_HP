import parsing_S001 as s001
from pprint import pprint
import time
import json

def modules_param_list(limit=None, sleep=1):
    # собираем список словарей по параметрам
    i = 0
    modules_param_list = []
    for module_led_url in s001.find_led_moduls(limit):
        modules_param_list.append(s001.module_info(module_led_url))
        time.sleep(sleep)
        i += 1
        print(i)
    return modules_param_list

def write_json(data, file_name="export/temp_db"):
    """
    Функция для экспорта' полученных данных в JSON файл.
    :param data: Экспортируемые файлы в формате dict
    :param file_name: Имя файла. По умолчанию = temp_db
    :return: сообщение, что данные экспортированы.
    """
    with open(file_name, 'w', encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        return print(f"Файлы успешно загружены в файл {file_name}")


write_json(modules_param_list(sleep=0.5))
# pprint(modules_param_list(limit=3, sleep=0.5))

# Тестирование
# i = 0
# # for module_led_url in s001.find_led_moduls():
# for i in range(21):
#     # i += 1
#     print(i)
#     time.sleep(2)
#
#     pprint(s001.module_info("/catalog/svetodiodnye_moduli_qiangli/ulichnye/q_seriya/svetodiodnyy_modul_qiangli_q10_320_160_outdoor.html"))
#
