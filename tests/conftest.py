import pytest 
import sqlite3
from django.db import connections
from django.core.management import call_command
from django.conf import settings
DBNAME = "test_db.sqlite3"

def run_sql(sql):
        conn = sqlite3.connect(f"{settings.BASE_DIR}/{DBNAME}")
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"]["NAME"] = DBNAME
    run_sql(f"DROP DATABASE IF EXISTS {DBNAME}")
    # run_sql('CREATE DATABASE the_copied_db TEMPLATE the_source_db')

    yield
    for connection in connections.all():
        connection.close()
    run_sql(f"DROP DATABASE {DBNAME}")

@pytest.fixture(scope="session")

def db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "fixture.json")
