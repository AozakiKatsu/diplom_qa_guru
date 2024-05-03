<h1> Проект по тестированию интернет-магазина "KazanExpress"</h1>

> <a target="_blank" href="https://kazanexpress.ru/">Ссылка на сайт</a>
![This is an image](design/images/main.png)
----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid

 ### Список проверок, реализованных в web/UI автотестах

- [x] Смена города выполняется
- [x] Поиск по сайту выполняется
- [x] Открывается по-ап авторизации
- [x] Проверка валидации ввода номера телефона
- [x] Добавление товара в избранное
- [x] Удаление товара из избранного
- [x] Добавление товара в корзину
- [x] Удаление товара из корзины

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/14hw_aozaki/">Ссылка на проект в Jenkins</a>
#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/14hw_aozaki/">проект</a>
2. Нажать кнопку `Build`
3. Результат запуска сборки можно посмотреть в отчёте Allure
----
### Allure отчет


#### Общие результаты
![This is an image](design/images/allure_report.png)
#### Список тест кейсов в Allure TestOps
![This is an image](design/images/allure-testops.png)
#### Нотификация в Telegram
![This is an image](design/images/бот.png)
#### Видео прохождения теста
![This is an video](design/images/video.mp4)

