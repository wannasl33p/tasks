## Курс Python

Привет! Добро пожаловать на курс по питону! 

Курс погрузит вас в питон и покажет его с разных сторон. 

Всего за время курса вы решите около 12и еженедельных наборов задач и 3 большие домашки.  
Каждая из них имеет public тесты, которые вы можете проверить самостоятельно и некоторые имеют private тесты, которые будут проверяться только на сервере.
А так же каждая из них будет проверяться на стиль и тайпинги.

Важно отметить, что сам курс осознанно проводится в среде максимально приближенной к реальной работе: 
используется git, gitlab, pytest, etc. - всё это является его частью и нужно будет с этим разбираться.

NB: до того как что-то делать **прочитайте эту инструкцию** (послушать лекцию так же желательно) 

### Структура 

Технически курс состоит из нескольких частей

![](images/gitlab-manytask-schema.png)

* [py.manytask.org](https://py.manytask.org)  
  Это web обёртка над гугл табличкой (ссылка на страничке). 
  Здесь вы можете видеть все доступные задачки, дедлайны и свои баллы. 
* [gitlab.manytask.org](https://gitlab.manytask.org/)  
  Наш инстанс gitlab где будет находиться ваш личный репозиторий и запускаться тесты.  
* [публичный репозиторий](https://gitlab.manytask.org/python/public-2022-fall)  
  Репозиторий в который регулярно выкладываются новые задачки (или фиксы к старым)  
  В процессе настройки вы подключите его как апстрим для обновления и получения новых задачек  
* [ваш личный репозиторий]  
  Основная точка работы с курсом - решения задачек и их проверки. 
  Является форком от публичного репозитория.  
  Репозиторий вы получите **автоматически** в процессе регистрации, вам нужно будет его только скопировать в Локальный репозиторий. 
* [gitlab runner](https://docs.gitlab.com/runner/)  
  Система запуска докер контейнеров где и будет запускаться ваш код.  
  Результаты и логи проверки будут доступны во вкладке CI/CD вашего репозитория


### Регистрация и настройка 

Чтобы решать и сдавать задачки курса вам нужно будет сделать несколько действий 
* Зарегистрироваться в manytask
* Настроить доступ к gitlab.manytask.org
* Установить питон и необходимые пакеты
* Научиться отправлять задачки на проверку

Всё это подробно описано в файле [`SETUP.md`](./SETUP.md), пожалуйста, **прочитайте его внимательно** перед тем как что-либо делать.


### Как контрибьютить в наш репозиторий

Мы за проактивный подход, поэтому если вы видите неточность или ошибку в условии задачи/тестах 
или хотите сделать новую задачку, то мы будем рады видеть ваши правки!

С любой правкой можно создать Issue или Merge Request (лучше его). 
Через некоторое время мы придём и обязательно его посмотрим. 
А дальше, или прокомментируем и обсудим с вами правки, или сразу примем. 

Подробную инструкцию можно найти в файле [`CONTRIBUTING.md`](CONTRIBUTING.md)


### Решение проблем 

Далее представлена короткая инструкция для ситуации `У меня всё сломалось!`

В первую очередь стоит самостоятельно попробовать разобраться в причинах ошибки. Самые рабочие варианты:  

* внимательное чтение логов (часто там написано почему именно упало)
* 'метод пристального взгляда'
* google 
* [`FAQ.md`](FAQ.md) (решения для самых частых проблем)

Если же вышеописанные методы не помогают - чатик ждёт вашего вопроса!

```
-А что делать если вообще всё получается?  
-Отвечать на вопросы в чатике! Это очень ценно!   
```

### Лекции

Записи лекций выкладываются в lk через несколько дней после очной лекции. 

Слайды лекции выкладываются в репозиторий в начале лекции и представляют собой интерактивные [jupyter notebooks](https://jupyter.org/) и могут быть запущены у вас.  

Всё это подробно описано в файле [`SETUP.md`](./SETUP.md)