import flet as ft
import variables

def main(page: ft.Page):
    page.title = 'Sistema de Estoque'
    page.height = 600
    page.width = 400

    page.add(variables.rola)
    page.update()

ft.app(main)