import flet as ft
import variables

def main(page: ft.Page):
    page.title = 'Sistema de Estoque'
    page.window.height = 600
    page.window.width = 400

    page.add(ft.Text(variables.teste))
    page.update()

ft.app(main)