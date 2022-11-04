import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from packaging import version
from selenium.webdriver.common.keys import Keys


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

        # self.assertIn("To-Do", self.driver.find_element(By.XPATH, '/html/body/logo').text)

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
        time.sleep(10)
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='id_list_table']")
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        # rows = table.find_elements(By.TAG_NAME, "tr")

        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        # self.assertTrue(
        #     any(row.text == '1: Купить павлиньи перья' for row in rows),
        #     f"Новый элемент списка не появился в таблице. Содержимым было:\
        # n{table.text}"
        # )

        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        inputbox = self.driver.find_element(By.CSS_SELECTOR, "input[id='id_new_item']")
        inputbox.send_keys("Сделать мушку из павлиньих перьев")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # (Эдит очень методична)
        # Страница снова обновляется, и теперь показывает оба элемента ее списка
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='id_list_table']")
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        self.assertIn("2: Сделать мушку из павлиньих перьев", [row.text for row in rows])

        self.check_list_items()


        # self.check_for_row_in_list_table('1: Купить павлиньи перья')
        # self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с объяснениями.
        self.fail("Finish the test!")
        # Она посещает этот URL-адрес – ее список по-прежнему там.
        # Удовлетворенная, она снова ложится спать.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
