from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page
from django.template.loader import render_to_string


# class HomePageTest(TestCase):
#
#     def test_root_url_resolves_to_home_page_view(self):
#         """Тест: корневой url преобразуется в представление
#            домашней страницы"""
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)
#
#     def test_home_page_returns_correct_html(self):
#         """Тест: домашняя страница возвращает правильный html"""
#         # request = HttpResponse()
#         # response = home_page(request)
#         # html = response.content.decode('utf8')
#         # self.assertTrue(html.startswith(html))
#         # self.assertIn('<logo>To-Do</logo>', html)
#         # self.assertTrue(html.strip().endswith('</html>'))
#         response = self.client.get('/')
#         html = response.content.decode('utf8')
#         self.assertTrue(html.startswith(html))
#         self.assertIn('<logo>To-Do</logo>', html)
#         self.assertTrue(html.strip().endswith('</html>'))
#         self.assertTemplateUsed(response, 'home.html')
#         #self.assertTemplateUsed(response, 'wrong.html')


class HomePageTest(TestCase):

    """Тест домашней страницы"""
    def test_uses_home_template(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


