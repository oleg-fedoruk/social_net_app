# SOCIAL NET APP

Для старта приложения с помощью docker-compose запустите скрипт start.sh. Скрипт применит миграции и
загрузит данные в базу данных. Приложение будет доступно по адресу localhost:8000.



```shell
./start.sh
```

В админку можно попасть с помощью следующих данных:
```
login: admin,
password:admin
```

По адресу ```localhost:8000/api/v1/user/<user_id:int>/events``` будет доступна
лента новостей для одного из трёх пользователей.

Для проверки запросов в Postman необходимо экспортировать файл [Social Net App.postman_collection.json](Social%20Net%20App.postman_collection.json)