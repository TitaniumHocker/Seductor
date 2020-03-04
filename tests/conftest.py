#! -*- coding: utf-8 -*-
from seductor import create_app
from seductor.models import db
import tempfile
import pytest
import os


@pytest.fixture
def client():
    app = create_app(mode='testing')
    temp_file = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{temp_file[1]}'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

    os.close(temp_file[0])
    os.unlink(temp_file[1])
