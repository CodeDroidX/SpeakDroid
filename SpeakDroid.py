print("\nЗагрузка SpeakDroid")
print("Привет от создателя https://github.com/CodeDroidX\n")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class SpeakDriver:
    def __init__(self,visible=False,logging=False):
        options = webdriver.ChromeOptions()
        if not visible: options.add_argument('--headless')
        if not logging: options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        try:
            self.driver = webdriver.Chrome(options=options)
        except:
            raise ValueError("Не надйен драйвер Chrome, он нужен для фонового запуска синтезатора. https://chromedriver.chromium.org/home Скачайте его .exe и поместите в рабучую папку")
        self.driver.get("https://translate.yandex.ru/")
    def Say(self,text: str):
        assert type(text)==type("string")
        ActionChains(self.driver)\
            .key_down(Keys.CONTROL)\
            .send_keys("a")\
            .key_up(Keys.CONTROL)\
            .key_down(Keys.DELETE)\
            .key_up(Keys.DELETE)\
            .perform()

        ActionChains(self.driver)\
            .send_keys(text)\
            .perform()

        time.sleep(0.4)
        ActionChains(self.driver)\
            .key_down(Keys.ALT)\
            .send_keys("v")\
            .key_up(Keys.ALT)\
            .perform()
        button=self.driver.find_element(By.ID,"textSpeaker")
        while button.get_attribute("class")!="boxButton boxButton_tts button button_view_clear button_size_l button_icn button_round state-silent":
            time.sleep(0.01)
    def exit(self):
        self.driver.quit()
if __name__=="__main__":
    d=SpeakDriver()
    d.Say("Если вы это слышите, то я исправна и готова к работе!")
    d.Say("Импортируйте этот модуль в своей программе и создайте объект драйвера")
    d.exit()
    exit()
def demo():
    print("Подготовка, запуск драйвера...")
    d=SpeakDriver()
    print("Говорю...")
    d.Say("Эй, проверка связи!")
    d.Say("Если ты это слышишь, то ты молодец")
    d.exit()
