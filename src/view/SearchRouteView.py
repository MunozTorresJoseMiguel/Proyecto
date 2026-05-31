import flet as ft

from src.models.RutaModel import RutaModel
from src.components.RouteCard import RouteCard


def SearchRouteView(page, user):

    def volver_dashboard(e):
        from src.view.dashboardView import DashboardView

        page.clean()
        page.add(
            DashboardView(page, user)
        )
        page.update()

    ruta_model = RutaModel()

    buscador = ft.TextField(
        label="Buscar calle o parada",
        width=500
    )

    btn_volver = ft.ElevatedButton(
        "⬅ Volver",
        on_click=volver_dashboard
    )

    resultados = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def buscar(e):

        resultados.controls.clear()

        rutas = ruta_model.buscar_rutas_por_parada(
            buscador.value
        )

        if not rutas:

            resultados.controls.append(
                ft.Text(
                    "No se encontraron rutas",
                    color="white",
                    size=20
                )
            )

        else:

            for ruta in rutas:

                resultados.controls.append(
                    RouteCard(
                        ruta["nombre_ruta"],
                        ruta["descripcion"],
                        "img/5A.jpg"
                    )
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
                ft.Row(
                    [btn_volver],
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Text(
                    "Buscar rutas",
                    size=30,
                    color="white",
                    weight="bold"
                ),

                buscador,

                ft.ElevatedButton(
                    "Buscar",
                    on_click=buscar
                ),

                resultados
            ],

            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    )