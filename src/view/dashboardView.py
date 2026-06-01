import flet as ft
from src.components.RouteCard import RouteCard


def DashboardView(page, user):
    from src.view.SearchRouteView import SearchRouteView

    def abrir_busqueda(e):

        page.clean()

        page.add(
        SearchRouteView(page,user)
    )

        page.update()
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
                    f"Bienvenido  {user['nombre']}",
                    size=35,
                    weight="bold",
                    color="white"
                ),
                
                ft.Text(
                    "Selecciona tu ruta",
                    size=20,
                    color="white"
                    
                ), 
                ft.ElevatedButton(
                    "buscar rutas",
                    on_click=abrir_busqueda
                ),

                ft.Container(height=20),

                ft.Row(

                    [
                        RouteCard(
                            "Ruta Centro",
                            "Centro - Pronaf",
                            "img/talamas.jpg"
                        ),

                        RouteCard(
                            "Ruta ITCJ",
                            "Las Torres - ITCJ",
                            "img/centro.jpg"
                        ),
                        RouteCard(
                            "Ruta 5-A",
                            "blv zaragoza - walmart",
                            "img/ruta.jpg"
                        ),
                        RouteCard(
                            "Ruta UNITEC",
                            "blv zaragoza - utcj",
                            "img/unitec.jpg"
                        ),
                        RouteCard(
                            "Ruta Centro",
                            "Centro - Pronaf",
                            "img/talamas.jpg"
                        ),

                        RouteCard(
                            "Ruta ITCJ",
                            "Las Torres - ITCJ",
                            "img/centro.jpg"
                        ),
                        RouteCard(
                            "Ruta 5-A",
                            "blv zaragoza - walmart",
                            "img/ruta.jpg"
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