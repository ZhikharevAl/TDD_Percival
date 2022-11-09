import unittest
import time
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
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

        self.driver.get(self.live_server_url)


        #  Она видит, что заголовок и шапка страницы говорят о
        #  списках неотложных дел.


        # Ей сразу предлагается ввести элемент списка
        inputbox = self.driver.find_element(By.CSS_SELECTOR, "input[id='id_new_item']")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a to-do item"
        )
        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
        # вязание рыболовных мушек)
        inputbox.send_keys("Купить павлиньи перья")
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='id_list_table']")
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])

        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        inputbox = self.driver.find_element(By.CSS_SELECTOR, "input[id='id_new_item']")
        inputbox.send_keys("Сделать мушку из павлиньих перьев")
        inputbox.send_keys(Keys.ENTER)
        # (Эдит очень методична)
        # Страница снова обновляется, и теперь показывает оба элемента ее списка
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='id_list_table']")
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')


        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с объяснениями.
        self.fail("Finish the test!")
        # Она посещает этот URL-адрес – ее список по-прежнему там.
        # Удовлетворенная, она снова ложится спать.

    def wait_for_row_in_list_table(self, row_text):
        """Ожидать строку в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.XPATH, "//tbody/tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:

                    raise e
                time.sleep(0.5)



# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
