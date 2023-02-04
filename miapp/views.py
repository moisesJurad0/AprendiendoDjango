"""Urls module."""

from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador
# MVT = Modelo Vista Template

layout_comun = """
<h1>Sitio web con Django | Moisés Jurado</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):
    """sumary_line."""
    html = """
        <h1>Inicio</h1>
        <br/>
        Años hasta el 2050
        <ul>
        """

    year = 2022
    while year <= 2050:
        html += f"<li>{year}</li>"
        year += 1
    html += "</ul>"

    return HttpResponse((layout_comun, html))


def hola_mundo(request):
    """sumary_line."""
    html = """<h1>Hello World ;D</h1>
            <h3>saludos.</h3>"""

    return HttpResponse(('', layout_comun, html))


def contacto(request, nombre='', apellidos=''):
    """sumary_line."""
    html = f"<h1>Contacto {nombre} {apellidos}</h1>"

    return HttpResponse(('', layout_comun, html))
