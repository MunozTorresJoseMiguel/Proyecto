import flet as ft
from src.components.RouteCard import RouteCard


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

                ft.Container(height=30),
                
                ft.Text(
                    f"BienvenidO{user['nombre']}",
                    size=35,
                    weight="bold",
                    color="white"
                ),

                ft.Container(height=20),

                ft.Row(

                    [

                        RouteCard(
                            "Ruta Centro",
                            "Centro - Pronaf",
                            "img/ruta1.jpg"
                        ),

                        RouteCard(
                            "Ruta ITCJ",
                            "Las Torres - ITCJ",
                            "img/ruta1.jpg"
                        ),
                        RouteCard(
                            "Ruta 5-A",
                            "blv zaragoza - walmart",
                            "img/5.A.jpg"
                        ),
                        RouteCard(
                            "Ruta UNITEC",
                            "blv zaragoza - utcj",
                            "img/unitec.jpg"
                        )

                    ],

                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER

                )

            ],

            expand=True,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        )

    )