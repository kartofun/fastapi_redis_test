## Задание 1

Необходимые предустановленные пакеты:

```
    docker-compose
```

Что нужно сделать для запуска:

* скачать/склонировать репозиторий
* перейти в папку с репозиторием
* запустить компоновку с помощью `docker-compose`: 

```
    docker-compose build
```
* опционально можно прогнать тесты:

```
docker-compose run --rm main_app py.test fastapiredis/tests.py --cov=fastapiredis
```
* после компоновки образа можно запустить:

```
    docker-compose up
```


Запущенный сервис будет доступен по адресу `http://0.0.0.0:8000`,  документация `http://0.0.0.0:8000/docs`






## Задание 2

Перенос данных о статусе из таблицы `short_names` в таблицу `full_names`:


```
UPDATE full_names SET status = table_res.status FROM (
    SELECT name_full, status, s_name  from (
        SELECT name as name_full, REGEXP_SUBSTR(name, '([^.]+)') as s_name from full_names
    ) as table1 JOIN short_names on table1.s_name = short_names.name
) as table_res
WHERE full_names.name = table_res.name_full
```

Генерация данных для тестов:

```
INSERT INTO short_names(name) SELECT CONCAT('names_', cast(i as varchar(16))) FROM generate_series(0, 700000) as t(i)

INSERT INTO full_names(name) SELECT concat(name, '.mp3') FROM short_names limit 500000

UPDATE short_names SET status = RANDOM()*10+1

```