import flet as ft
from src.view.dashboardView import DashboardView

def go_dashboard(page, user):
    page.controls.clear()
    page.add(DashboardView(page, user))
    page.update()
    
def RecoverView(page, auth_controller):

    correo_input = ft.TextField(
        label="Correo",
        width=350
    )

    nueva_pass_input = ft.TextField(
        label="Nueva contraseña",
        password=True,
        width=350
    )

    def cambiar_password(e):

        success, msg = auth_controller.recuperar_password(
            correo_input.value,
            nueva_pass_input.value
        )
        if success:
            go_dashboard(page, {"nombre": correo_input.value})
            page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True
        page.update()

    return ft.Container(

        expand=True,

        content=ft.Column(

            [

                ft.Text(
                    "Recuperar contraseña",
                    size=35,
                    color="white"
                ),

                correo_input,

                nueva_pass_input,

                ft.ElevatedButton(
                    "Cambiar contraseña",
                    on_click=cambiar_password
                )

            ],

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        ),

        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#0f172a", "#1d4ed8"]
        )

    )