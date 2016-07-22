# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import Home


@pytest.mark.nondestructive
def test_open_home_page(base_url, selenium):
    page = Home(selenium, base_url).open()
    assert page.is_logo_displayed
    assert 'Welcome to {{cookiecutter.name}}' == page.welcome
