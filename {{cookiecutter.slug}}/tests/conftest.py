# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest


@pytest.fixture(scope='session')
def session_capabilities(session_capabilities):
    # add or modify session capabilities here
    return session_capabilities


@pytest.fixture
def capabilities(capabilities):
    # modify test method capabilities here
    return capabilities


@pytest.fixture
def firefox_path(firefox_path):
    # modify the firefox path here
    return firefox_path


@pytest.fixture
def firefox_profile(firefox_profile):
    # modify the firefox profile here
    return firefox_profile
