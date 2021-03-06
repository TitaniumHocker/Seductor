#! -*- coding: utf-8 -*-
from flask import current_app as app
from seductor.models import Link, Visit
from seductor.logger import logger
from seductor import db
from typing import List
import base62 as b62
import qrcode


def get_by_id(link_id: int) -> object:
    link = Link.query.filter_by(id=link_id).first()
    logger.info(f'{__name__}.get_by_id {link_id} => {link}')
    return link


def get_by_url(url: str) -> object:
    link = Link.query.filter_by(original_url=url).first()
    logger.info(f'{__name__}.get_by_url {url} => {link}')
    return link


def create(url: str, create_qr: bool = True) -> object:
    link = Link(original_url=url)
    db.session.add(link)
    db.session.commit()
    db.session.refresh(link)
    logger.info(f'{__name__}.create {url} => {link}')
    if create_qr:
        _generate_qr_code(link)
    return link


def register_visit(link: object, remote_host: str) -> None:
    visit = Visit(host=remote_host)
    link.visits.append(visit)
    db.session.commit()
    logger.info(f'{__name__}.register_visit to {link} from {remote_host}')
    return


def get_top() -> List[dict]:
    raw_top = Link.query.\
            outerjoin(Link.visits).\
            group_by(Link.id).\
            order_by(db.func.count(Visit.id).desc()).\
            limit(100).all()
    logger.info(f'{__name__}.get_top: len => {len(raw_top)}')
    data = [
        {'id': link.id,
         'original_url': link.original_url,
         'visits_count': link.visits.count()}
        for link in raw_top]
    logger.debug(f'{__name__}.get_top: {data}')
    return data


def _generate_qr_code(link: object) -> None:
    link_url = (f'{app.config["BASE_URL"]}/'
                f'{app.config["LINK_PREFIX"]}'
                f'{b62.encode(link.id)}')
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
    img.save(f'seductor/static/img/{app.config["QR_CODE_PREFIX"]}'
             f'{b62.encode(link.id)}.png')
    logger.info(f'{__name__}._generate_qr_code for {link}')
    return
