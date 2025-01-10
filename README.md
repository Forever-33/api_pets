## Тестирование api сервиса https://petstore.swagger.io/ (pytest+requests+allure)

### ```./cases.md``` - Тест-кейсы для сервиса

### ```./api``` - Директория сервисов api
### ```./api/pet``` - Директория сервиса api - pet
### ```./api/pet/api_pet``` - Описание методов для взаимодействия с api - pet
### ```./api/pet/endpoints``` - Описание эндпоинтов для api - pet
### ```./api/pet/payloads``` - Описание тел запросов для api - pet
### ```./api/pet/models``` - Директория с описанием моделей тел ответа при использовнии Pydantic
### ```./config/base_test.py``` - Использование классов страниц для тестов
### ```./config/headers.py``` - Заголовки запросов и ответов для тестов
### ```./tests``` - Директория с тестами
### ```./utils/helper.py``` - Хелпер, служащий для добавления response в allure отчет
### ```./conftest.py``` - Настройка и конфигурация тестов

### ```./requirements.txt``` - Используемые пакеты в проекте
### ```./pytest.ini``` - Конфигурация выполнения тестов

#### Установка зависимостей
``` 
pip install -r requirements.txt
```

#### Запуск тестов и генерация allure отчетности
``` 
pytest -v --alluredir=./allure-results
```

#### Запуск allure отчета
``` 
allure serve ./allure-results  
```