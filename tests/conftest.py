#! -*- coding: utf-8 -*-
from seductor import create_app
from seductor.models import db
import tempfile
import pytest
import os


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    tmp_db = tempfile.mkstemp()
    print(tmp_db)
    db_fd = tmp_db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{tmp_db[1]}'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

    os.close(db_fd[0])
    os.unlink(tmp_db[1])
