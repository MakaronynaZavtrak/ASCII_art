# ASCII Art Converter

Консольное приложение для преобразования изображений в ASCII-арт с поддержкой цветного (ANSI) и черно-белого режимов.

## Возможности

- Преобразование изображений в ASCII-арт
- Поддержка цветного (ANSI) и черно-белого режимов
- Настраиваемые размеры выходного изображения
- Сохранение результата в файл или вывод в консоль
- Поддержка различных форматов изображений (PNG, JPEG, и др.)

## Установка

1. Клонируйте репозиторий:
```bash
  git clone https://github.com/Knkydd/ASCII-Art.git
 ```
2. Создайте виртуальную среду и активируйте её:
```bash
  python -m venv .venv
 ```

# Windows
```bash
  .venv\Scripts\activate
```

# Linux/macOS
```bash
  source .venv/bin/activate
```

3. Установите зависимости:
```bash
  pip install -r requirements.txt
```


## Использование


### Базовое использование
```bash
  python src/main.py path/to/image.jpg
```


### С указанием выходного файла
```bash
  python src/main.py path/to/image.jpg output.txt
```

### С дополнительными параметрами
```bash
  python src/main.py --input path/to/image.jpg --output result.txt --width 100
```


### Параметры командной строки

- `input` - путь к входному изображению
- `output` - путь для сохранения результата (необязательно)
- `--width` - ширина выходного ASCII-изображения (по умолчанию: 720)
- `--height` - высота выходного ASCII-изображения (по умолчанию: пропорционально ширине)

## Примеры

### Черно-белый режим
При запуске программы выберите опцию 'G' для создания черно-белого ASCII-арта:
```What type of ascii do you want? [C/c - Colourful] | [G/g - Grayscale]```<br>
```>>> G```


### Цветной режим (ANSI)
Выберите опцию 'C' для создания цветного ASCII-арта с использованием ANSI-цветов:
```What type of ascii do you want? [C/c - Colourful] | [G/g - Grayscale]```<br>
```>>> C```


## Структура проекта

```
ASCII-art/ 
├── ASCIIArtist.py    # Основной класс для конвертации изображений
├── main.py           # Точка входа в приложение 
├── settings.py       # Настройки и константы 
├── requirements.txt  # Зависимости проекта
├── README.md        # Документация проекта
└── test/
    └── test_ascii_artist.py  # Модульные тесты
```

### Описание файлов:

- `ASCIIArtist.py` - содержит основной класс для преобразования изображений в ASCII-арт
- `main.py` - обработка аргументов командной строки и запуск приложения
- `settings.py` - конфигурация логгера и константы приложения
- `test_ascii_artist.py` - юнит-тесты для проверки функциональности

## Зависимости

- Python 3.13.1+
- Pillow >= 10.2.0 - для обработки изображений
- NumPy >= 1.26.4 - для работы с массивами

## Запуск тестов
```bash
  python -m unittest tests/test_ascii_artist.py
```

## Лицензия
MIT License

Copyright (c) 2025 <Semenov Oleg, Pesterev Alexandr>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Авторы

Семенов Олег - [GitHub](https://github.com/MakaronynaZavtrak)

Пестерев Александр - [GitHub](https://github.com/Knkydd)