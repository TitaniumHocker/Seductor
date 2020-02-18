#! -*- coding: utf-8 -*-
from ..models import Link, Visit
from ..app import app, db, logger
import base62 as b62
import qrcode


BASE_URL = f'{app.config["SCHEME"]}://{app.config["DOMAINS"][-1]}'

def get_by_id(link_id):
    link = Link.query.filter_by(id=link_id).first_or_404()
    logger.debug(f'controller.link.get_by_id {link_id} => {link}')
    return link

def get_by_url(url):
    link = Link.query.filter_by(original_url=url).first()
    logger.debug(f'controller.link.get_by_url {url} => {link}')
    return link

def create(url):
    link = Link(original_url=url)
    db.session.add(link)
    db.session.commit()
    db.session.refresh(link)
    logger.debug(f'controller.link.create {url} => {link}')
    _generate_qr_code(link)
    return link

def register_visit(link, remote_host):
    visit = Visit(host=remote_host)
    link.visits.append(visit)
    db.session.commit()
    logger.debug(f'controller.link.register_visit to {link} from {remote_host}')
    return True

def get_top():
    top = Link.query.order_by(Link.visits).all()
    logger.debug(f'controller.link.get_top')
    print(top)
    return top

def _generate_qr_code(link):
    link_url = f'{BASE_URL}/{b62.encode(link.id)}'
    qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2
            )
    qr.add_data(link_url)
    qr.make(fit=True)
    img = qr.make_image(
            fill_color='#800000',
            back_color='#e6e6e6'
            )
    img.save(f'seductor/static/img/{b62.encode(link.id)}.png')
    logger.debug(f'controller.link._generate_qr_code {link}')
