# Тест-кейсы для веб-версии Discord

## 1. Отправка/удаление/редактирование сообщений

### 1.1 Отправка сообщений

#### Тест-кейс 1.1.1: Отправка текстового сообщения

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
-   **Ожидаемый результат**: Сообщение отображается в канале.

#### Тест-кейс 1.1.2: Отправка сообщения с упоминанием пользователя

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст с упоминанием пользователя (@user) в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
-   **Ожидаемый результат**: Сообщение отображается с упоминанием пользователя.

#### Тест-кейс 1.1.3: Отправка сообщения с упоминанием роли

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст с упоминанием роли (@role) в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
-   **Ожидаемый результат**: Сообщение отображается с упоминанием роли.


### 1.2 Редактирование сообщений

#### Тест-кейс 1.2.1: Редактирование текста сообщения

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
    **Сообщение отображается в канале.**
    3. Нажать на кнопку, открывающую меню действий у сообщения.
    4. Нажать на кнопку "Редактировать" в меню действий.
    5. Изменить текст сообщения.
    6. Нажать кнопку "Enter" на клавиатуре.
    7. Проверить наличие метки "отредактировано" под сообщением.
-   **Ожидаемый результат**: Сообщение отображается с новым текстом и Метка"отредактировано" отображается под сообщением.

### 1.3 Удаление сообщений

#### Тест-кейс 1.3.1: Удаление собственного сообщения

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
    **Сообщение отображается в канале.**
    3. Нажать на кнопку, открывающую меню действий у сообщения.
    4. Нажать на кнопку "Удалить" в меню действий.
-   **Ожидаемый результат**: Сообщение исчезает из канала.

## 2. Добавление/удаление реакций к сообщениям

### 2.1 Добавление реакций

#### Тест-кейс 2.1.1: Добавление стандартной реакции

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
    **Сообщение отображается в канале.**
    3. Нажать на кнопку, открывающую меню действий у сообщения.
    4. Нажать на кнопку добавления реакции.
-   **Ожидаемый результат**: Реакция добавляется к сообщению.

#### Тест-кейс 2.1.2: Добавление нескольких реакций к одному сообщению

-   **Предусловия**: Пользователь авторизован и находится в канале.
-   **Шаги**:
    1. Ввести текст в поле ввода сообщения.
    2. Нажать кнопку "Enter" на клавиатуре.
    **Сообщение отображается в канале.**
    3. Нажать на кнопку, открывающую меню действий у сообщения.
    4. Нажать на кнопку добавления реакции.
    **Меню действий закрылось**
    5. Нажать на кнопку, открывающую меню действий у сообщения.
    6. Нажать на кнопку добавления реакции. 
-   **Ожидаемый результат**: Реакции добавляются к сообщению.