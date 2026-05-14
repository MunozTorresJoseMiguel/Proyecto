import flet as ft

from src.view.LoginView import LoginView
from src.controller.userController import AuthController


def main(page: ft.Page):

    page.title = "JuarezGO"
    page.window_width = 400
    page.window_height = 750
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    auth_controller = AuthController()

    login_view = LoginView(page, auth_controller)

    page.add(login_view)


ft.run(main)