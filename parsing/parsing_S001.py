import bs4
import requests
from fake_useragent import UserAgent
from pprint import pprint
BASE_URL = "https://ledcapital.ru"
HEADERS = {'User-Agent': UserAgent().chrome}

def response_site(URL):
    response = requests.get(URL, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    return soup

def find_led_moduls(limit=None):
    """
    Функция находит все необходимые позиции (модули LED) в разделе сайта, и выдаёт их адреса.
    :param limit: Задаётся кол-во позиций начиная с первой, которые необходимо выгрузить.
                  Если параметр не указан, то будут выгружены все найденные позиции.
    :return: Возвращается список URL найденных позиций
    """
    URL = BASE_URL + "/catalog/svetodiodnye_moduli_qiangli/"
    bs4_list_led_moduls = response_site(URL).find_all(class_="name", limit=limit)
    list_led_moduls = []
    for moduls_div in bs4_list_led_moduls:
        list_led_moduls.append(moduls_div.find("a").attrs["href"])  # Забираем URL модуля и добавляем в список
    return list_led_moduls

def module_info(url_module):
    """
    Функция находит на конкретном сайте все параметры конкретного товара и собирает их один словарь.
    :param url_module: Обязательный входной параметр - URL товара (указывается без BASE_URL - FQDN сайта)
    :return: Возвращает словарь с разделением на Параметр (key) и Значение (Value).
    """
    response = response_site(BASE_URL + url_module)
    module_param = response.find(id="tab2").find(class_="text")
    price = response.find(class_="product-item-detail-price-current mb-1").get_text()
    # что бы получить данные src нужно полученный список найденных результатов разделить на отдельные элементы
    image_list = [BASE_URL + image['src'] for image in response.find(id="sync2").find_all("img")]
    param_all_list = module_param.get_text(strip=True, separator='\n').splitlines()
    param_dict = {}
    param_dict["Цена"] = price.replace('\xa0', "")      # replace('\xa0', "") убирает пробел после тысячи
    param_dict["Изображения"] = image_list
    for param in param_all_list:
        param_list = param.split(sep=':')
        param_dict[param_list[0]] = param_list[1]
    return param_dict

# response = response_site("https://ledcapital.ru/catalog/svetodiodnye_moduli_qiangli/ulichnye/q_seriya/svetodiodnyy_modul_qiangli_p10_krasnyy.html")

# response = response_site("https://ledcapital.ru/catalog/svetodiodnye_moduli_qiangli/ulichnye/q_seriya/svetodiodnyy_modul_qiangli_q4_eco_320_160_outdoor.html")
# module_param = response.find(id="tab2").find(class_="text")
# param_all_list = module_param.get_text(strip=True, separator='\n').splitlines()
# pprint(param_all_list)
