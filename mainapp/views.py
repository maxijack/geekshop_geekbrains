import datetime
import json
import os
from django.shortcuts import render
from django.conf import settings


def get_data_from_json(file_name):
    static_url = os.path.join(settings.BASE_DIR, 'static/json/' + file_name)
    with open(static_url, 'r', encoding='utf-8') as jsonFile:
        json_data = json.load(jsonFile)
        jsonFile.close()

    return json_data


def main(request):
    products_data = get_data_from_json('products.json')

    title = "главная"
    content = {"title": title, "products": products_data}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    links_menu = get_data_from_json('links_menu.json')
    same_products = get_data_from_json('same_products.json')
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
