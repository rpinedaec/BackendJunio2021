import logging
from flask import abort, render_template, redirect, url_for
from flask_login import current_user
from app.models import Producto
from .forms import CommentForm
from . import public_bp


logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    #logger.info('Mostrando los posts del blog')
    return render_template("public/index.html")


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Producto.get_all()
    return render_template("public/index.html", posts=posts)
