from django.test import TestCase, RequestFactory
from hamcrest import *
from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest
from kantasker.views import HomePageView
from mock import *

class TestKantaskerHomePage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_root_url_resolves_to_home_page(self):
        result = resolve('/')
        assert_that(result.func, same_instance(HomePageView))

    def test_homepage_return_correct_html(self):
        expected_title = b'<title>Kantasker - Welcome</title>'
        expected_start_tag = b'<!DOCTYPE html>'
        expected_end_tag = b'</html>'

        request = self.factory.get('/')
        result = HomePageView.as_view()(request).render()

        assert_that(result.content, starts_with(expected_start_tag))
        assert_that(result.content, contains_string(expected_title))
        assert_that(result.content, ends_with(expected_end_tag))

    def test_homepage_use_correct_template(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        result = response.template_name[0]

        expected = 'home_page.html'
        assert_that(result, is_(expected))
        assert_that(response.status_code, is_(200))
