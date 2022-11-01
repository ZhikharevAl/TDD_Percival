import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from packaging import version


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """Установка"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        """Демонтаж"""
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""

        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу.

        base_url = "http://127.0.0.1:8000/"
        self.driver.get(base_url)

        #  Она видит, что заголовок и шапка страницы говорят о
        #  списках неотложных дел.

        self.assertIn("To-Do", self.driver.find_element(By.XPATH, '/html/body/logo').text)
        self.fail("Закончить тест!")

        # Ей сразу предлагается ввести элемент списка
        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
        # вязание рыболовных мушек)
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        # Страница снова обновляется, и теперь показывает оба элемента ее списка
        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с объяснениями.
        # Она посещает этот URL-адрес – ее список по-прежнему там.
        # Удовлетворенная, она снова ложится спать.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
