dept приложение отображающее работу Сарансккабель.БНиЭ

--Создать модели:
    !+Сотрудники:
      должность
      ФИО,
      дата рождения,
      дата приема на работу,
      телефон,
      адрес,
      !-график работы основной
      !-график работы внеурочной (заносить выходные и празд. дни, а также выходы в смену за кого то)

    +Отпуска:
      тип: планируемый, фактический
      Сотрудник
      !-год
      дата начала
      дата окончания
      кол-во дней


    Работа внеурочная:
      год
      сотрудник
      дата начала
      дата окончания или кол-во дней

    Отгулы и выходные
      сотрудник
      дата  начала
      дата окончания или кол-во дней
      кол-во часов

    График работы:
      Название
      Тип работы(8 или 12)
      Первый день работы в 1 смену
      структура = 'dnww'='день, ночь, выходной, выходной'

    !-Должность:
      +Название,
      +Описание,
      !-Зарплата
      Ссылка на должностную инструкцию

--На странице вывести поле с отображением даты, времени, номере смены,
  список сменного персонала в день и ночь
  (можно указать мелким шрифтом ночную до и ночную после, если тек. время ночь
  то дневные смены)

  ------------------------макет------------------------------------------------
12 ноября 2016 - Смена - №2
Сменный мастер : Иванов
Инженер электроник: Петров

  ------------------------макет конец------------------------------------------

--Подготовить макет страницы

--Создать модель для ведения дел

--Создать модель для ведения заметок:
    Заголовок
    Текст
    Цвет
    Статус-Срочно, Обычно, Завершено, Удалено

определение тек смены,
  чтение даты начала смен, - 4шт.
  определение тек даты.
  получение разности тек.даты и даты начала
  разделить на 4 если, остаток =0 то это тек смена.

формат даты для отображения в html: https://docs.djangoproject.com/en/1.10/ref/templates/builtins/

как делать свои фильтры для сайта http://stackoverflow.com/questions/4651172/reference-list-item-by-index-within-django-template/29664945#29664945

01.04.17
Для каждого рабочего составить массив дней для года [0..356] c описание графика работы, учета отпсков, и так-далее