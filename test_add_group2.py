from application import Application
import pytest


@pytest.fixture
def app():
    fixture = Application()

    return fixture


def test_login(app):
    app.login('admin', '10Uyjvjd.')








