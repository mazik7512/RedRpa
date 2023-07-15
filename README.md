# Проект RedRpa 

**RedRPA - Framework** - библиотека с открытым исходным кодом на Python, предназначенная для разработки RPA-роботов.

- [Проект RedRpa](#проект-redrpa)
- [Состав проекта](#состав-проекта)
- [Описание](#описание)
  * [Ядро. SDK. Язык сценариев (RSL)](#ядро-sdk-язык-сценариев-(rsl))
  * [Ядро. SDK. Компилятор](#ядро-sdk-компилятор)
  * [Ядро. SDK. REX](#ядро-sdk-rex)
  * [Ядро. SDK. Red Virtual Machine](#ядро-sdk-red-virtual-machine)
  * [Ядро. SDK. Набор библиотек языка RSL](#ядро-sdk-набор-библиотек-языка-rsl)




![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


# Состав проекта

В проекте реализованы:

1. RedRPA - Framework.
   
   1.1. Сетевые протоколы и менеджер работы с сетью.
   
   1.2. Шифрование *(RSA, AES512)* и хэширование *(ГОСТ 34.11)*.
   
   1.3. Комплект средств разработки сценариев *(SDK - Scenario Development Kit)*.
   
      - Компилятор языка сценариев **RSL** *(Red Scenario Language)*.
   
      - Набор API - библиотек для языка **RSL**.
   
      - Виртуальная машина *(RVM - Red Virtual Machine)*.
   

   1.4. Модуль машинного зрения на основе нейронной сети *(OpenCV + Tensorflow + Tesseract OCR)*.
  
   1.5. Модуль взаимодействия с Web - окружением *(Selenium Web Driver)*.
  
   1.6. Модуль взаимодействия с Windows *(WinAPI + PyWin32)*.
  
2. Клиентское приложение.
   
3. Серверное приложение.
   

# Описание

Структура библиотеки представляет из себя "связку" **Ядра (Core)** и внешних модулей **(External Modules)**. Ядро в свою очередь будет состоять из внутренних модулей и включать в себя основные абстракции для обеспечения гибкости, расширяемости и взаимозаменяемости внешних и внутренних модулей, а также платформо-независимые и независящие от внешних библиотек механизмы, обеспечивающие функционирование фреймворка *(шифрование, хеширование, сетевые функции, компилятор, виртуальная машина, логирование и система исключений)*.

Подсистема внешних модулей будет включать в себя платформо-зависимые и реализуемые с помощью сторонних библиотек механизмы: 
   -	модуль для взаимодействия с Windows, 
   -	модуль взаимодействия с Web-окружением,
   -	модуль компьютерного зрения.

## Ядро. SDK. Язык сценариев (RSL)
Ниже представленна грамматика языка RSL в расширенной форме Бэкуса-Наура.
```
SCENARIO := LINES
LINES := LINE | LINES
LINE := SPECIAL_INSTRUCTION | FUNC_DEFINITION | EXPR, ENDLINE
EXPR := ASSIGMENT | FUNC_CALL
SPECIAL_INSTRUCTION := LOOP | RETURN
ASSIGMENT := OBJECT, ASSIGMENT_OPERATION, (EXPR | LITERAL | OBJECT)
FUNC_CALL := OBJECT, FUNC_CALL_ARG_LIST
FUNC_DEFINITION := FUNC_DEFINITION_HEADER, FUNC_DEFINITION_BODY
FUNC_DEFINITION_HEADER := function, TEXT, FUNC_DEF_ARG_LIST
FUNC_DEF_ARG_LIST := SUBEXPR_START, {(FUNC_DEF_ARG[ARG_DELIMITER])}, SUBEXPR_END
FUNC_DEF_ARG := OBJECT
FUNC_DEFINITION_BODY := BODY
FUNC_CALL_ARG_LIST := SUBEXPR_START, {(FUNC_CALL_ARG[ARG_DELIMITER])}, SUBEXPR_END
FUNC_CALL_ARG := STANDART_CALL_ARG
RETURN := return, [RETURN_ARG], ENDLINE
RETURN_ARG := STANDART_CALL_ARG
STANDART_CALL_ARG := FUNC_CALL | OBJECT | LITERAL
LOOP := LOOP_HEADER, LOOP_BODY
LOOP_HEADER := loop, SUBEXPR_START, LOOP_HEADER_ARG, SUBEXPR_END
LOOP_HEADER_ARG := NUMBER | FUNC_CALL | OBJECT
LOOP_BODY := BODY
BODY := BODY_START, BODY_LINES, BODY_END
BODY_LINES := {BODY_LINE}
BODY_LINE := SPECIAL_INSTRUCTION | EXPR, ENDLINE
OBJECT := RESERVED_NAMES | USER_OBJECT
USER_OBJECT := TEXT
LITERAL := ", TEXT, " | NUMBER
TEXT := {CHARACTER}, {NUMBER} | TEXT
NUMBER := [SIGN]{DIGIT} | [SIGN]{DIGIT}, ., {DIGIT}
SUBEXPR_START := (
SUBEXPR_END := )
BODY_START := {
BODY_END := }
ARG_DELIMITER := ,
ASSIGMENT_OPERATION := =
ENDLINE := ;
SIGN := -
RESERVED_NAMES := стандартные функции (CV_scan, click_on_object...)
CHARACTER := алфавит(a,b...)
DIGIT := цифры(0,1,2...)
```
Основными конструкциями языка являются: 
   - `SPECIAL_INSTRUCTION` - "специальные" встроенные инструкции `loop`, `return` *(цикл, и возврат значения из функции соотвественно)*.
   - `FUNC_DEFINITION` - ключевое слово `function`, используемое для определения функций в пользовательском коде.
   - `EXPR` - так называемое "выражение". Под выражение понимается либо операция присвоения `a = foo()`, `a = 5`.


Все имена *(функции, переменные)* в грамматике языка представлены в конструкцией `OBJECT`.

RSL также поддерживает числовые *(целые и с плавающей точкой)* и строковые литералы.

Пример сценарий на языке RSL:
```
function foo(a, b){
  b = a = 42;
  return b;
}
c = 3;
loop(2){
  c = foo(c, 1);
}
```

## Ядро. SDK. Компилятор

Компиляция состоит из 6 этапов:
1.	Лексический анализ.
2.	Синтаксический анализ.
3.	Семантический анализ.
4.	Процесс связывание имён.
5.	Трансляция.
6.	Линковка.
 
Этап компиляции           | Выходные данные
------------------------- | ----------------------------------------------------------------------------------
Лексический анализ        | Массив лексемм *(токенов)* / список лексических ошибок
Синтаксический анализ     | Абстрактное синтаксическое дерево *(далее - AST)* / список синтаксических ошибок
Семантический анализ      | AST / список семантических ошибок
Процесс связывание имён   | AST + секции импорта и инициализации / список ошибок процесса связывания имён
Трансляция                | Секция пользовательского кода
Линковка                  | **REX** - Red Executable

## Ядро. SDK. REX

REX - является исполняемым файлом Red Virtual Machine. Структура файла являет собой секции *(по-умолчанию 4)*.

   - Секция информации.
   - Секция импорта.
   - Секция инициализации.
   - Секция пользовательского кода.

**Секция информации** содержит в себе метаданные о исполняемом файле *(хэш остальных секций, номер версии, стандарт реализации)* и генерируются после создания всех остальных секций. 

**Секции импорта и инициализации** генерируются в процессе компиляции на этапе связывания имён - предназначение этих секций довольно очевидно (они содержат данные о подключаемых модулях, и их инициализации соотвественно). 

**Секция пользовательского кода** содержит скомпилированный код языка RSL (что тоже довольно очевидно).
Секции представлены в виде json - структуры.

## Ядро. SDK. Red Virtual Machine

RVM принимает на вход файлы формата REX и анализирует их. Первоначально производится контроль целостности файла путем сравнения хэшей. Далее секции импорта, инициализации и пользовательского когда передаются на выполнение. В данном случае выполнением занимается Python, так как RSL по-умолчанию транслируется именно в него.

## Ядро. SDK. Набор библиотек языка RSL

На данный момент в фреймворке реализованы три библиотеки языка RSL:
   1. Универсальная *(на основе машинного зрения)* - позволяет работать с любыми приложениями.
   2. Web - позволяет взаимодействовать с Web - приложениями.
   3. General - набор общих функций, не связанных с автоматизацией напрямую.
