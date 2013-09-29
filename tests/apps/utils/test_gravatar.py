from django.test import TestCase
from apps.utils.gravatar import get_gravatar_link, DEFAULT_SIZE
from hamcrest import *


class TestGetGravatarLink(TestCase):
    def setUp(self):
        self.base_url_http = 'http://www.gravatar.com/avatar/'
        self.base_url_https = 'https://secure.gravatar.com/avatar/'
        self.default_size = DEFAULT_SIZE
        self.link_template = "{url}{hash}?s={size}&d={default}"

    def generate_expected_gravatar(self, email_hash, default='mm', size=None, is_https=False):
            expected_size = size if size else self.default_size
            expected_url = self.base_url_https if is_https else self.base_url_http
            expected = self.link_template.format(
                url=expected_url,
                hash=email_hash,
                default=default,
                size=expected_size
            )
            return expected

    def test_gravatar_for_empty_mail(self):
        email = None
        expected = self.generate_expected_gravatar('00000000000000000000000000000000')
        result = get_gravatar_link(email)
        assert_that(result, equal_to(expected))



    def test_gravatar_for_normal_mail(self):
        email = 'krkmetal@gmail.com'
        expected = self.generate_expected_gravatar('fafa6e91aafb9444528f3b44eb3c3cf4')
        result = get_gravatar_link(email)
        assert_that(result, equal_to(expected))

    def test_gravatar_for_another_size(self):
        email = None
        size = 150
        expected = self.generate_expected_gravatar(
            '00000000000000000000000000000000',
            size=size)
        result = get_gravatar_link(email, size=size)
        assert_that(result, equal_to(expected))

    def test_gravatar_for_another_default(self):
        email = None
        expected = self.generate_expected_gravatar(
            '00000000000000000000000000000000',
            default='monsterid')
        result = get_gravatar_link(email, default_image_index=2)
        assert_that(result, equal_to(expected))