**Развёртывание RabbitMQ** <br />
Во время тестирования RabbitMQ был запущен в Docker контейнере, он разворачивается через Docker Compose.
Для того, чтобы развернуть сервис, нужно открыть командную строку в той же папке, что и файл ```docker-compose.yaml```
и прописать следующие команды:
- docker compose pull
- docker compose up -d rabbitmq

Теперь можно зайти в графический интерфейс RabbitMQ в браузере по адресу ```localhost:15672```

**Развёртывание загрузчика и потребителя** <br />
Для загрузчика и потребителя нужно отдельно создать файлы ```.env```, их содержание будет идентичным:
- ```RMQ_HOST``` - хост, на котором развёрнут RabbitMQ
- ```RMQ_PORT``` - порт, по которому общается RabbitMQ (именно RabbitMQ, а не менеджер)
- ```RMQ_USER``` - логин пользователя для доступа к RabbitMQ
- ```RMQ_PASSWORD``` - пароль пользователя для доступа к RabbitMQ
- ```QUEUE_NAME``` - название очереди, с которой будет работать приложения

**Работа загрузчика (producer)** <br />
Загрузчик запускается консольной командой ```python main.py <ссылка на страницу>```,
введённая ссылка проверяется на корректность, после чего все внутренние ссылки записываются в очередь

**Работа потребителя (consumer)** <br />
Особых условий для запуска потребителя нет. В variables.py можно задать две переменных:
- ```TIMEOUT``` - время ожидания сообщения в секундах, если очередь пуста.
После завершения таймаута приложения останавливается
- MAX_LINKS - максимальное количество страниц, по которым парсер будет искать их внутренние сслыки.
Это было сделано для того, чтобы на больших сайтах в очереди гарантированно заканчивались сообщения

**Логирование** <br />
В обеих частях приложения при парсинге сайтов прочитанные внутренние ссылки логируются в консоль.
Потребитель помимо этого возвращает информацию о прочтении сообщения из очереди