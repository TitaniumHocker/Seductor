#! -*- coding: utf-8 -*-
from seductor.models import Link, Visit
from seductor import app, db, logger
from typing import List
import base62 as b62
import qrcode


BASE_URL = f'{app.config["SCHEME"]}://{app.config["DOMAINS"][-1]}'

def get_by_id(link_id: int) -> object:
    link = Link.query.filter_by(id=link_id).first()
    logger.debug(f'{__name__}.get_by_id {link_id} => {link}')
    return link

def get_by_url(url: str) -> object:
    link = Link.query.filter_by(original_url=url).first()
    logger.debug(f'{__name__}.get_by_url {url} => {link}')
    return link

def create(url: str) -> object:
    link = Link(original_url=url)
    db.session.add(link)
    db.session.commit()
    db.session.refresh(link)
    logger.debug(f'{__name__}.create {url} => {link}')
    _generate_qr_code(link)
    return link

def register_visit(link: object, remote_host: str) -> None:
    visit = Visit(host=remote_host)
    link.visits.append(visit)
    db.session.commit()
    logger.debug(f'{__name__}.register_visit to {link} from {remote_host}')
    return

def get_top() -> List[dict]:
    raw_top = Link.query.\
            outerjoin(Link.visits).\
            group_by(Link.id).\
            order_by(db.func.count(Visit.id).desc()).\
            limit(100).all()
    logger.debug(f'{__name__}.get_top: len => {len(raw_top)}')
    return [{
        'id': link.id,
        'original_url': link.original_url,
        'visits_count': link.visits.count()} for link in raw_top]

def _generate_qr_code(link: object) -> None:
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
    logger.debug(f'{__name__}._generate_qr_code for {link}')
    return
