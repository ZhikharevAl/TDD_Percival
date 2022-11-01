from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Тест: корневой url преобразуется в представление
           домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Тест: домашняя страница возвращает правильный html"""
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<logo>To-Do lists</logo>', html)
        self.assertTrue(html.strip().endswith('</html>'))
