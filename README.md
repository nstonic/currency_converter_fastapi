# Конвертер валют по курсу ЦБ

## Как развернуть local-окружение
Для запуска ПО вам понадобятся Docker и Docker Compose. Инструкции по их установке ищите на официальных
сайтах:

- [Install Docker Desktop](https://www.docker.com/get-started/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

Сначала соберите докер-образ с помощью Docker Сompose:

```shell
$ docker compose build
```

Запустите докер-контейнеры:

```shell
$ docker compose up
```


## Как использовать

Конвертировать валюты можно запросом: \
[/api/rates/?from=USD&to=RUB&value=3](http://127.0.0.1:8000/api/rates/?from=USD&to=RUB&value=3) 

Свагер доступен по [ссылке](http://127.0.0.1:8000/docs/)