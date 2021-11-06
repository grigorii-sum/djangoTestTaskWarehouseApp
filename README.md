# djangoTestTaskWarehouseApp
Проект "djangoTestTaskWarehouseApp" является одним из двух приложений для решения тестовой задачи.

Задача заключается в том, чтобы реализовать двустороннюю синхронизацию данных между двумя приложениями посредством REST API (следовательно, добавление/изменение/удаление информации посредством http-запросов).

---

Приложение Warehouse App (djangoTestTaskWarehouseApp) имеет следующий функционал:

- http://127.0.0.1:8002/warehouse-order/create/ - создание WarehouseOrder (запрос на создание обычно приходит от Store App при создании StoreOrder)
- http://127.0.0.1:8002/warehouse-order/update/<str:pk>/ - изменение WarehouseOrder и отправка запроса на изменение StoreOrder
- http://127.0.0.1:8002/warehouse-order/update-from-store/<str:pk>/ - метод для изменения WarehouseOrder (запрос об изменении приходит от Store App при изменении StoreOrder)
- http://127.0.0.1:8002/warehouse-order/delete/<str:pk>/ - удаление WarehouseOrder и отправка запроса на удаление StoreOrder
- http://127.0.0.1:8002/warehouse-order/detail/<str:pk>/ - просмотр WarehouseOrder

---

## ЗАПУСК ПРОЕКТА

Введите последовательно все нижеперечисленные команды:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver 8002`

Проект запущен.
