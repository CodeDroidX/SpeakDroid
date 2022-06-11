# SpeakDroid
Python imp. of Neural network TTS in yandex translator

![image](https://user-images.githubusercontent.com/52743561/173181931-1ecebfa0-831c-42c2-b710-26538e554e90.png)

Для решения проблемы компьютерной речи есть множество разных либ, например __pyttsx3__ и __GTTS__

Я использовал обе и могу сказать что голос в __pyttsx__ совсем убогий

А __GTTS__ использует интернет и гугл переводчик, при этом имеет всё еще роботизированный акцент

## Для серьёзных задач используется платный __Yandex SpeechKit API__
### Он использует неросейть и посмотреть пример его работы можно в Yandex переводчике
### Увы, он платный

> Мне жалко деньги, что мне делать?
> 
> __Озвучивать текст в Yandex переводчике...__
> 
> Но как это автоматизировать?
### Взять Selenium, python и мой драйвер.
# 1 Шаг
```cmd
pip install selenium
```
# 2 Шаг
Скачиваем .exe ChromeDriver в рабочую папку с официального сайта https://chromedriver.chromium.org/home
# 3 Шаг
```python
import SpeakDroid
SpeakDroid.demo() # Быстрый тест работы

driver=SpeakDroid.SpeakDriver()
driver.Say("Я хороший, я хороший")
driver.exit()
