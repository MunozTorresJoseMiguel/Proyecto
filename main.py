import flet as ft

from src.view.LoginView import LoginView
from src.controller.userController import AuthController


def main(page: ft.Page):
    page.window.maximized = True
    page.title = "JuarezGO"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    auth_controller = AuthController()

    login_view = LoginView(page, auth_controller)

    page.add(login_view)


ft.run(main)