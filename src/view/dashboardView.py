import flet as ft


def DashboardView(page):

    return ft.View(
        route="/dashboard",
        controls=[

            ft.AppBar(
                title=ft.Text("Dashboard")
            ),

            ft.Text(
                "LOGIN CORRECTO",
                size=40
            )

        ]
    )