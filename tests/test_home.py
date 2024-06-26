from typing import Tuple
from api.data.register import User

from pages.home_page import HomePage
from .fixtures import logged_in_test, chrome_browser # used


def test_successful_login(logged_in_test: Tuple[HomePage, str, User]):
    home_page, token, user = logged_in_test
    home_page.verify_header(user.firstName)
