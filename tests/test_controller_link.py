#! -*- coding:utf-8 -*-
from seductor import controller as ctl
from tests.conftest import client as c
import base62 as b62


def test_get_link_by_id(c):
    link = ctl.link.create('https://cocainum.ru')
    assert ctl.link.get_by_id(link.id) == link


def test_get_link_by_url(c):
    url = 'https://cocainum.ru'
    link = ctl.link.create(url)
    assert ctl.link.get_by_url(url) == link


def test_create(c):
    url = 'https://cocainum.ru'
    assert ctl.link.create(url).id == 1


def test_register_visit(c):
    url = 'https://cocainum.ru'
    link = ctl.link.create(url)
    assert c.get(f'{b62.encode(link.id)}').status_code == 302
    assert link.visits.count() == 1


def test_get_top_simple(c):
    urls = [
        'https://cocainum.ru',
        'https://morphine.ru',
        'https://heroin.ru'
    ]
    for url in urls:
        ctl.link.create(url)

    assert len(ctl.link.get_top()) == 3
