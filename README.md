# divination-bot
## Описание проекта
Divination Bot — это Telegram-бот для гадания по книгам. Пользователь загадывает вопрос, выбирает книгу, страницу и строку, после чего бот: возвращает строчку (с учётом границ предложения); определяет тональность предсказания; выводит эмоции, характерные для текста; оценивает, насколько предсказание уникально относительно всей книги; предлагает похожие слова для интерпретации смысла предсказания; показывает персональную и общую статистику.

Важно: бот носит развлекательный характер, его предсказания не следует воспринимать всерьёз!
## Структура репрозитория
### Препроцессинг:
- ```books```: файлы с расширением ```.pdf```, на основе которых выводятся предсказания в боте
- ```db```: файлы, относящиеся к базе данных
- ```create.py```: создание структуры базы данных
- ```lemmatize.py```: лемматизация
- ```load_books.py```: заполнение базы данных информацией о книгах
- ```pdf_to_text.py```: парсинг книг (извлечение текста построчно по страницам)
### Код бота:
- ```bot.py```: основная логика Telegram-бота
- ```context.py```: поиск полного предложения по выбранной строке
- ```sentiment.py```: анализ тональности, эмоций, сравнение с предыдущими предсказаниями
- ```similar.py```: поиск похожих слов с помощью модели Word2Vec
- ```unique.py```: оценка уникальности предсказания
- ```stats.py```: вывод графиков со статистикой
## Деплой
Бот выложен на платформу [pythonanywhere](https://abelyayeva.pythonanywhere.com/8788891470:AAFr487oaCLT4rj2EU2lg6QNFahORJo0W_o). Файлы этой версии бота (кроме базы данных) можно увидеть в папке ```for_paw```. Бот намного лучше работает, если его запустить из Google Collab (если собираетесь запускать, напишите нам, чтобы приостановить хостинг на pythonanywhere).

## Как запустить локально?
Мы работали в python 3.12.13. 

**Чтобы запустить бот со своего ПК, необходимо:**
- открыть [тетрадь в Google Colab](https://colab.research.google.com/drive/1y58i3D2aVeipnrPXIPjo-UHuL0pknsid?usp=sharing);
- скопировать её к себе на диск;
- **загрузить в файлы тетрадки:** [базу данных](https://drive.google.com/file/d/1rBCUXmGlKrAe59FZshQJAKjpe_muI-hL/view?usp=sharing), [context.py](https://github.com/chugcha/divination-bot/blob/main/context.py), [lemmatize.py](https://github.com/chugcha/divination-bot/blob/main/lemmatize.py), [sentiment.py](https://github.com/chugcha/divination-bot/blob/main/sentiment.py), [similar.py](https://github.com/chugcha/divination-bot/blob/main/similar.py), [stats.py](https://github.com/chugcha/divination-bot/blob/main/stats.py), [unique.py](https://github.com/chugcha/divination-bot/blob/main/unique.py), [requirements.txt](https://github.com/chugcha/divination-bot/blob/main/requirements.txt), [sentiment.py](https://github.com/abelyayeva/divination-bot/blob/91c2caff6e850d62767fbf59f056b24c641e54c3/sentiment.py);
- запустить ячейку с requirements;
- запустить ячейку для активации бота.
  
Пока ячейка работает, телеграм-бот активен и им можно пользоваться.

**Важно!** 
Если вы решили закончить работу с ботом, **необходимо запустить ячейку "Деактивация бота".** 
Когда в этой ячейке отобразится "True", можно закрывать блокнот.
## Команда
- [Александра Беляева](https://github.com/abelyayeva), тг: @a_belyayeva
- [Кира Чугаева](https://github.com/chugcha), тг: @melodeclamatorr
- [Елизавета Боголюбская](https://github.com/lizaveta-b), тг: @liza_veta_b
