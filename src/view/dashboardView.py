import flet as ft

def DashboardView(page, user):

    return ft.Container(

        expand=True,

        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#0f172a", "#1d4ed8"]
        ),

        content=ft.Column(

            [

                ft.Icon(
                    ft.Icons.DIRECTIONS_BUS,
                    size=100,
                    color="white"
                ),

                ft.Text(
                    "BIENVENIDO A JUAREZGO",
                    size=40,
                    weight="bold",
                    color="white"
                ),

            ft.Text(
                "LOGIN CORRECTO",
                size=40
            ),
            ft.TextButton(
                    "Cerrar Sesion",
                     on_click=lambda e: LoginOut(),
                        style=ft.ButtonStyle(color="white")
                    )

            ],
            expand=True,

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        )

    )