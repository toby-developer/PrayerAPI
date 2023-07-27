from bs4 import BeautifulSoup
from datetime import datetime, date
import requests

kirill_headers = [
    "Ҳафта куни",
    "Тонг(Саҳарлик)",
    "Қуёш",
    "Пешин",
    "Аср",
    "Шом(Ифтор)",
    "Хуфтон",
]

uzbek_headers = [
    "Hafta kuni",
    "Tong(Saharlik)",
    "Quyosh",
    "Peshin",
    "Asr",
    "Shom(Iftor)",
    "Xufton",
]

english_headers = ["Weekday", "Fajr", "Sunrise",
                   "Dhuhr", "Asr", "Maghrib", "Isha"]

kirill_weekdays = [
    "Душанба",
    "Сешанба",
    "Чоршанба",
    "Пайшанба",
    "Жума",
    "Шанба",
    "Якшанба",
]

uzbek_weekdays = [
    "Dushanba",
    "Seshanba",
    "Chorshanba",
    "Payshanba",
    "Juma",
    "Shanba",
    "Yakshanba",
]

english_weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def translate_headers(header, language):
    """
    Translates the given header to the specified language.
    """
    header_index = kirill_headers.index(header)
    suited_headers = uzbek_headers if language == "uz" else english_headers
    return suited_headers[header_index]


def translate_weekdays(text, language):
    """
    Translates the given weekday text to the specified language.
    """
    try:
        weekday_index = kirill_weekdays.index(text)
        suited_weekdays = uzbek_weekdays if language == "uz" else english_weekdays
        return suited_weekdays[weekday_index]
    except ValueError:
        return text


def get_region_names_by_language(language):
    """
    Returns a dictionary containing region names in the specified language.
    """
    kirill_region_names = [
        "Андижон",
        "Бекобод",
        "Бишкек",
        "Бухоро",
        "Гулистон",
        "Денов",
        "Жалолобод",
        "Жамбул",
        "Жиззах",
        "Жомбой",
        "Каттақўрғон",
        "Конибодом",
        "Марғилон",
        "Навоий",
        "Наманган",
        "Нукус",
        "Нурота",
        "Самарқанд",
        "Туркистон",
        "Ўш",
        "Хива",
        "Хўжанд",
        "Чимкент",
        "Шаҳрихон",
        "Қарши",
        "Қўқон",
        "Тошкент",
        "Шеробод",
        "Хўжаобод",
        "Қўрғонтепа",
        "Хонобод",
        "Поп",
        "Чуст",
        "Косонсой",
        "Чортоқ",
        "Учқўрғон",
        "Фарғона",
        "Олтиариқ",
        "Риштон",
        "Қува",
        "Олмаота",
        "Сайрам",
        "Ангрен",
        "Бурчмулла",
        "Олот",
        "Газли",
        "Қоровулбозор",
        "Қоракўл",
        "Пахтаобод",
        "Зомин",
        "Дўстлик",
        "Арнасой",
        "Ўсмат",
        "Ғаллаорол",
        "Ғаллаорол",
        "Учтепа",
        "Ўғиз",
        "Томди",
        "Конимех",
        "Қизилтепа",
        "Зарафшон",
        "Узунқудуқ",
        "Учқудуқ",
        "Мингбулоқ",
        "Тўрткўл",
        "Тахтакўпир",
        "Чимбой",
        "Мўйноқ",
        "Олтинкўл",
        "Шуманай",
        "Қўнғирот",
        "Ургут",
        "Булоқбоши",
        "Термиз",
        "Қумқўрғон",
        "Бойсун",
        "Шеробод",
        "Урганч",
        "Хазорасп",
        "Хонқа",
        "Янгибозор",
        "Шовот",
        "Деҳқонобод",
        "Ғузор",
        "Косон",
        "Таллимаржон",
        "Муборак",
        "Душанбе",
        "Ашхабод",
        "Туркманобод",
        "Тошҳовуз",
    ]

    english_region_names = [
        "Andijan",
        "Bekobod",
        "Bishkek",
        "Bukhoro",
        "Guliston",
        "Denov",
        "Zhalolobod",
        "Zhambyl",
        "Jizzakh",
        "Jomboy",
        "Kattaqo'rg'on",
        "Konibodom",
        "Margilon",
        "Navoiy",
        "Namangan",
        "Nukus",
        "Nurota",
        "Samarkand",
        "Turkiston",
        "Ush",
        "Khiva",
        "Khujand",
        "Chimkent",
        "Shahrihon",
        "Qarshi",
        "Qo'qon",
        "Tashkent",
        "Sherobod",
        "Khujayobod",
        "Qo'rg'ontepa",
        "Khonobod",
        "Pop",
        "Chust",
        "Kosonsoy",
        "Chortoq",
        "Uchkurgon",
        "Fargona",
        "Oltiariq",
        "Rishton",
        "Kuva",
        "Olmaliq",
        "Sayram",
        "Angren",
        "Burchmulla",
        "Olot",
        "Gazli",
        "Qorovulbozor",
        "Qorako'l",
        "Pakhtaobod",
        "Zomin",
        "Dostlik",
        "Arnasoy",
        "Osmat",
        "Gallaorol",
        "Gallaorol",
        "Uchtepa",
        "Og'iz",
        "Tomdi",
        "Konimekh",
        "Qiziltepa",
        "Zarafshon",
        "Uzunquduk",
        "Uchkuduk",
        "Mingbulok",
        "Tortko'l",
        "Takhtakopir",
        "Chimboy",
        "Moynoq",
        "Oltinkol",
        "Shumanay",
        "Qo'ng'iro't",
        "Urgut",
        "Buloqbo'shi",
        "Termez",
        "Qumqo'rg'on",
        "Boysun",
        "Sherobod",
        "Urganch",
        "Khozarasp",
        "Honqa",
        "Yangibozor",
        "Shovot",
        "Dehqonobod",
        "Guzor",
        "Koson",
        "Tallimarjon",
        "Muborak",
        "Dushanbe",
        "Ashgabat",
        "Turkmanobod",
        "Toshhovuz",
    ]

    uzbek_region_names = [
        "Andijon",
        "Bekobod",
        "Bishkek",
        "Buxoro",
        "Gulistoni",
        "Denov",
        "Jalolobod",
        "Jambul",
        "Jizzax",
        "Jomboy",
        "Kattaqo'rg'on",
        "Konibodom",
        "Marg'ilon",
        "Navoiy",
        "Namangan",
        "Nukus",
        "Nurota",
        "Samarqand",
        "Turkiston",
        "Ush",
        "Xiva",
        "Xojand",
        "Chimkent",
        "Shahrixon",
        "Qarshi",
        "Qo'qon",
        "Toshkent",
        "Sherobod",
        "Xo'jayobod",
        "Qo'rg'ontepa",
        "Honobod",
        "Pop",
        "Chust",
        "Qosonsoy",
        "Chortoq",
        "Uchkurgon",
        "Farg'ona",
        "Oltiariq",
        "Rishton",
        "Quva",
        "Olmaliq",
        "Sairam",
        "Angren",
        "Burchmulla",
        "Olot",
        "Gazli",
        "Qorovulbozor",
        "Qorako'l",
        "Paxtaobod",
        "Zomin",
        "Dostlik",
        "Arnasoy",
        "Osmat",
        "Gallaorol",
        "Gallaorol",
        "Uchtepa",
        "O'g'iz",
        "Tomdi",
        "Konimex",
        "Qiziltepa",
        "Zarafshon",
        "Uzunquduq",
        "Uchquduq",
        "Mingbuloq",
        "To'rtko'l",
        "Taxtako'pir",
        "Chimboy",
        "Moynoq",
        "Oltinko'l",
        "Shumanay",
        "Qo'ng'iro't",
        "Urgut",
        "Buloqbo'shi",
        "Termiz",
        "Qumqo'rg'on",
        "Boysun",
        "Sherobod",
        "Urganch",
        "Xozorasp",
        "Honqa",
        "Yangibozor",
        "Shovot",
        "Dehqonobod",
        "G'uzor",
        "Koson",
        "Tallimarjon",
        "Muborak",
        "Dushanbe",
        "Ashxabod",
        "Turkmanobod"
        "To'shovuz",
    ]

    suited_region_names = (
        uzbek_region_names
        if language == "uz"
        else (
            english_region_names
            if language == "en"
            else (kirill_region_names if language == "cr" else english_region_names)
        )
    )

    regions_dict = {
        str(index): name for index, name in enumerate(suited_region_names, start=1)
    }

    regions_list = [
        {"id": int(key), "name": value} for key, value in regions_dict.items()
    ]
    return {
        "region_names": suited_region_names,
        "regions_list": regions_list,
        "regions_dict": regions_dict,
    }


def get_region_name_by_id(id, language):
    """
    Returns the name of the region corresponding to the given ID and language.
    """
    regions = get_region_names_by_language(language)["regions_dict"]
    return regions[f"{id}"]


def get_region_id_by_name(name, language):
    """
    Returns the ID of the region corresponding to the given name and language.
    """
    regions_list = get_region_names_by_language(language)["regions_list"]
    for region in regions_list:
        if region["name"] == name:
            return region["id"]
    return None


def get_monthly_prayer_times_for_region(region_id, month, language):
    """
    Retrieves the monthly prayer times for the specified region, month, and language.
    """
    # Fetch the HTML content of the website
    url = f"https://islom.uz/vaqtlar/{region_id}/{month}"
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find("table", class_="prayer_table")
    headers = [header.text.strip() for header in table.select("thead th")]
    rows = table.select("tbody tr")

    data = []
    for row in rows:
        cells = row.find_all("td")
        row_data = {}
        for i, cell in enumerate(cells):
            if headers[i] in kirill_headers:
                header = translate_headers(headers[i], language)
                if cell.text.strip() in kirill_weekdays:
                    row_data[header] = translate_weekdays(
                        cell.text.strip(), language)
                else:
                    row_data[header] = cell.text.strip()
        data.append(row_data)
    return data


def get_month_names(prayer_times):
    """
    Returns the month names in the given prayer times data.
    """
    return list(prayer_times[0].keys())[0:2]


def get_prayer_times_by_date(region_id, month, day, language):
    """
    Retrieves the prayer times for the specified region, month, day, and language.
    """
    prayer_times = get_monthly_prayer_times_for_region(
        region_id, month, language)
    return prayer_times[day - 1]


def get_message(region_id, month, day, language):
    """
    Generates a message with the prayer times for the specified region, month, day, and language.
    """
    this_year = date.today().year

    if language == "en":
        prayer_times = get_prayer_times_by_date(region_id, month, day, "en")
        region_name = get_region_name_by_id(region_id, "en")
        return f"""🕌 Today's Prayer Times 🌙

        🌍 Location: {region_name}

        🕋 Fajr: {prayer_times["Fajr"]}
        🌅 Sunrise: {prayer_times["Sunrise"]}
        ☀️ Dhuhr: {prayer_times["Dhuhr"]}
        🌇 Asr: {prayer_times["Asr"]}
        🌆 Maghrib: {prayer_times["Maghrib"]}
        🌃 Isha: {prayer_times["Isha"]}

        📅 Date: {this_year}-{month}-{day}

        May you have a blessed day filled with peace and devotion. 🙏🏼
        """
    elif language == "uz":
        prayer_times = get_prayer_times_by_date(region_id, month, day, "uz")
        region_name = get_region_name_by_id(region_id, "uz")
        return f"""🕌 Bugungi Namoz Vaqtlari 🌙

        🌍 Joylashuv: {region_name}

        🕋 Bomdod: {prayer_times["Tong(Saharlik)"]}
        🌅 Quyosh chiqishi: {prayer_times["Quyosh"]}
        ☀️ Peshin: {prayer_times["Peshin"]}
        🌇 Asr: {prayer_times["Asr"]}
        🌆 Shom: {prayer_times["Shom(Iftor)"]}
        🌃 Xufton: {prayer_times["Xufton"]}

        📅 Sana: {this_year}-{month}-{day}

        Kuningiz tinchlik va halovatga to'la bo'lsin. 🙏🏼
        """
    else:
        return "Unsupported language."