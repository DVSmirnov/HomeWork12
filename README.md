### ЗАПУСК ТЕСТОВ ЧЕРЕЗ DOCKERFILE
1. Запустить opencart, selenoid, selenoid-ui, загрузить браузеры с помощью команды "docker pull _browser_settings_". На ПК должен быть установлен allure
2. В директории проекта выполнить "docker build -t tests ."
   * В десктопном приложении docker появится образ (image) с тестами: 
   ![images/img.png](images/img.png)
3. Запуск контейнера с тестами с генерацией отчета: "docker run --name tests_run tests:latest && docker cp tests_run:/app/allure-results . && allure serve allure-results"
![images/img_1.png](images/img_1.png)

### JENKINS
#### Настройки джобы:
![images/jenkins/img_0.png](images/jenkins/img_0.png)
![images/jenkins/img_1.png](images/jenkins/img_1.png)
![images/jenkins/img_2.png](images/jenkins/img_2.png)
![images/jenkins/img_3.png](images/jenkins/img_3.png)
![images/jenkins/img_4.png](images/jenkins/img_4.png)

#### Запуск джобы:
![images/jenkins/img_5.png](images/jenkins/img_5.png)

#### Сгенерированный отчет:
![images/jenkins/img_6.png](images/jenkins/img_6.png)
