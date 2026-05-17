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
                    ft.Icons.DASHBOARD,
                    size=100,
                    color="white"
                ),

                ft.Text(
                    "BIENVENIDO A juarez GO",
                    size=40,
                    weight="bold",
                    color="white"
                ),

                ft.Text(
                    f"Bienvenido {user['nombre']}",
                    color="white70",
                    size=20
                )

            ],
            expand=True,

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        )

    )