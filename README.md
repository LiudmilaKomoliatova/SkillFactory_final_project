#SkillFactory final project

##Skillfactory курса INTQAP 1032 - Тестирование авторизации в личном кабинете Ростелеком Информационные Технологии 

+ Ссылка на личный кабенет: [b2c.passport.rt.ru](https://b2c.passport.rt.ru/)
+ Тест-кейсы доступны по ссылке: [test_cases](https://docs.google.com/spreadsheets/d/1pvK0n6bLbK7vG0fp66BP94rHOMjcpEqifCG31UethNM/edit?usp=sharing)
+ Баг-репорты доступны по ссылке: [bug reports](https://docs.google.com/spreadsheets/d/1g-NySFdM6FcLeuV6xE6nuvW4dTxi03H0BfmuBGCz-IY/edit?usp=sharing)

Запуск тестов:
>pytest -v --driver Chrome --driver-path driver.exe 

*В папке pages base_page.py - конструктор webdriver
*В папке pages auth_page.py, reg_page.py - тестовые классы
*В папке tests test_auth_page.py, test_reg_page.py - тесты
*В папке pages locators.py - локаторы
*В корне проекта conftest.py - фикстуры
*В корне проекта settings.py - переменные для параметризации тестов
