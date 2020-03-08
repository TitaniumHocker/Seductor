#! -*- coding: utf-8 -*-
from tests.conftest import client


def test_index(client):
    post_data = {'url': 'https://cocainum.ru'}
    assert client.get('/').status_code == 200
    assert client.post('/', data=post_data).status_code == 201
    assert client.post('/', data=post_data).status_code == 200


def test_about(client):
    assert client.get('/about').status_code == 200
    assert client.post('/about').status_code == 405


def test_stats(client):
    assert client.get('/stats').status_code == 200
    assert client.post('/stats').status_code == 405


def test_not_found(client):
    assert client.get('/where').status_code == 404
    assert client.get('/is').status_code == 404
    assert client.get('/my').status_code == 404
    assert client.get('/money').status_code == 404
