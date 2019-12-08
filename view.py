from app import *
from models import Links
from flask import request, render_template, redirect
import base62

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('original_url')
        link = Links(original_url=url)
        db.session.add(link)
        db.session.commit()
        db.session.refresh(link)
        short_url = f'http://192.168.0.14/{base62.encode(link.id)}'
        return f'<h1>{short_url}</h1>'


    return '''
    <form action="/" method="POST">
        <input type="url" name="original_url" placeholder="type your url here">
        <button type="submit">allah</button>
    </form>
    '''
    


@app.route('/top', methods=['GET'])
def top_page():
    return 'top page'


@app.route('/stats', methods=['GET', 'POST'])
def stats_page():
    return 'stats page'


@app.route('/about', methods=['GET'])
def about_page():
    return 'about page'


@app.route('/<magical_url>')
def magic(magical_url):
   link = Links.query.filter_by(id=base62.decode(magical_url)).first_or_404()
   print(link)
   return redirect(link.original_url)


@app.errorhandler(404)
def not_found_page(e):
    return '4040404040', 404


