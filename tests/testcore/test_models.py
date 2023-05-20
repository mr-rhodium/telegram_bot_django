import pytest
from django.contrib.auth import get_user_model
from tests.conftest import db_setup
def test_superuser(db_setup):
    user = get_user_model().objects.get(username="Admin")
    assert user.is_superuser