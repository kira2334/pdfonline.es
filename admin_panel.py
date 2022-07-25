from flask import Blueprint, send_file, render_template
from bd import obtener_conexion
admin_panel = Blueprint('admin_panel', __name__)

@admin_panel.route("/admin/")
def index_admin():
   return render_template("repos/admin_template/index.html")
@admin_panel.route("/admin/<path:ruta>")
def index_admin():
   return render_template("repos/admin_template/"+ ruta)