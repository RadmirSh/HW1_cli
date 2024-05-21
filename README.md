# HW1_cli

# Проверка вывода команды

Этот скрипт на Python можно использовать для выполнения команды в терминале и проверки наличия определенного текста или слова в выводе.

## Установка
Для этого скрипта не требуются дополнительные пакеты. Просто скопируйте и вставьте код в свою среду Python.

## Использование
1. checkcommandoutput(command, text, mode='line'): Эта функция принимает три параметра - command (команда для выполнения в терминале), text (текст или слово, которое нужно проверить в выводе) и mode (режим проверки - 'line' для проверки, содержится ли текст в строке вывода и 'word' для проверки присутствия слова в выводе).

2. Использование скрипта:
```
import subprocess
import string

def check_command_output(command, text, mode='line'):
    # Код функции здесь

-- Пример использования:
command = "ls -l"
text = "file.txt"
print(check_command_output(command, text))
``````

## Пример
Скрипт гибкий и позволяет пользователям указать, хотят ли они проверить определенную строку текста в выводе или искать конкретное слово. Параметр mode может быть соответственно настроен.