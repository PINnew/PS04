from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Инициализация браузера
browser = webdriver.Firefox()

# Переход на главную страницу Википедии
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

try:
    # Ожидание загрузки элементов с тегом 'div' и атрибутом класса 'hatnote'
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'hatnote'))
    )

    hatnotes = []

    # Поиск всех элементов 'div' на странице
    for element in browser.find_elements(By.TAG_NAME, 'div'):
        cl = element.get_attribute('class')
        # Проверка, содержит ли класс 'hatnote'
        if 'hatnote' in cl:
            hatnotes.append(element)

    # Если элементы с классом 'hatnote' найдены, выбираем случайный
    if hatnotes:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, 'a').get_attribute('href')
        browser.get(link)
        print(link)
    else:
        print("Элементы с классом 'hatnote' не найдены.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера через некоторое время
    browser.quit()
