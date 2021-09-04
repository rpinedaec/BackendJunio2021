
from app.models import Producto
import logging
from operator import methodcaller
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from app.auth.models import User
# from app.models import Post
from . import admin_bp
from .forms import ProductosForm, UserAdminForm

logger = logging.getLogger(__name__)


@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    return render_template("admin/index.html")




@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_users():
    users = User.get_all()
    return render_template("admin/users.html", users=users)


@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required #son decoradores 
@admin_required
def update_user_form(user_id):
    # Aquí entra para actualizar un usuario existente
    user = User.get_by_id(user_id) # Sql alchemy
    # select * from User where id = user_id
    if user is None:
        logger.info(f'El usuario {user_id} no existe')
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del usuario.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Actualiza los campos del usuario existente
        user.is_admin = form.is_admin.data
        user.role_id = form.role.data
        user.save()
        logger.info(f'Guardando el usuario {user_id}')
        return redirect(url_for('admin.list_users'))
    return render_template("admin/user_form.html", form=form, user=user)


@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(user_id):
    logger.info(f'Se va a eliminar al usuario {user_id}')
    user = User.get_by_id(user_id)
    if user is None:
        logger.info(f'El usuario {user_id} no existe')
        abort(404)
    user.delete()
    logger.info(f'El usuario {user_id} ha sido eliminado')
    return redirect(url_for('admin.list_users'))

#La logica que va a tener el html
@admin_bp.route("/products/insert/<int:user_id>", methods=['GET', 'POST'])
@login_required
def form_products(user_id):
    user = User.get_by_id(user_id)
    form = ProductosForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        stock = form.stock.data
        precio = form.precio.data
        categoria = form.categoria_id.data
        Producto.insertProduct(nombre,stock,precio,categoria)
        #redirect("index.html")
    return render_template("admin/insert_productos.html",form = form)

@admin_bp.route("/products/list/", methods=['GET', 'POST'])
@login_required
def list_products():
    productos = Producto.get_all()
    return render_template("admin/list_products.html",productos = productos)