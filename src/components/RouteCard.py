import flet as ft

def RouteCard(titulo, descripcion, imagen):

    return ft.Card(

        elevation=10,

        content=ft.Container(

            width=420,
            padding=15,

            content=ft.Column(

                [

                    ft.Image(
                        src="img/ruta1.jpg",
                        width=400,
                        height=260,
                        border_radius=12
                    ),

                    ft.Text(
                        titulo,
                        size=22,
                        weight="bold"
                    ),

                    ft.Text(
                        descripcion
                    ),

                    ft.ElevatedButton(
                        "Ver ruta"
                    )

                ]

            )

        )

    )