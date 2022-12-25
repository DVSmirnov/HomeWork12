FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 /app

ENTRYPOINT ["rm", "allure-results"]
ENTRYPOINT ["pytest", "--remote"]

# docker build -t tests . (создание образа с тестами)
# docker run --name tests_run tests:latest && docker cp tests_run:/app/allure-results . && allure serve allure-results  (запуск контейнера с тестами)
# docker run --name tests_run tests:latest --browser firefox && docker cp tests_run:/app/allure-results . && allure serve allure-results (запуск тестов с параметрами)