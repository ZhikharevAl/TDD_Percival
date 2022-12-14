from lists.models import Item
from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """Тест: можно сохранить запрос POST"""
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """Тест: переадресует после post-запроса"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

    def test_displays_all_list_items(self):
        """Тест: отображаются все элементы списка"""
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
    """Тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_item_saved = saved_items[0]
        second_item_saved = saved_items[1]
        self.assertEqual(first_item_saved.text, 'The first (ever) list item')
        self.assertEqual(second_item_saved.text, 'Item the second')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохраняет элементы, только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
