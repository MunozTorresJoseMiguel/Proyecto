from src.view.dashboardView import DashboardView
import flet as ft

def go_dashboard(page, user):
    page.controls.clear()
    page.add(DashboardView(page, user))
    page.update()
    
def RegisterView(page, auth_controller):

    nombre_input = ft.TextField(
        label="Nombre",
        width=350,
        border_radius=12,
        filled=True,
        bgcolor="#1e293b",
        color="white",
        border_color="#3b82f6"
    )

    correo_input = ft.TextField(
        label="Correo",
        width=350,
        border_radius=12,
        filled=True,
        bgcolor="#1e293b",
        color="white",
        border_color="#3b82f6"
    )

    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=12,
        filled=True,
        bgcolor="#1e293b",
        color="white",
        border_color="#3b82f6"
    )
    
    def registrar_click(e):

        success, msg = auth_controller.registrar(
            nombre_input.value,
            correo_input.value,
            pass_input.value
        )
        if success:
            
            user = {"nombre": nombre_input.value}
            go_dashboard(page, user)
            
            page.clean()
            page.add(DashboardView(page, user))
            page.update()
            
        else:
            page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )
            page.snack_bar.open = True
            page.update()
        
    def abrir_login():
        from src.view.LoginView import LoginView
        page.clean()
        page.add(
        LoginView(page, auth_controller)
    )
           
    return ft.Container(

        expand=True,

        alignment=ft.Alignment(0, 0),

        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#0f172a", "#1d4ed8"]
        ),

        content=ft.Column(

            [
                
                
                

                ft.Icon(
                    ft.Icons.PERSON_ADD,
                    size=90,
                    color="white"
                ),

                ft.Text(
                    "Crear Cuenta",
                    size=40,
                    weight="bold",
                    color="white"
                ),

                ft.Container(height=20),

                nombre_input,

                correo_input,

                pass_input,

                ft.Container(height=10),
                
                ft.TextButton(
                "¿Ya tienes cuenta? Inicia sesión",
                on_click=lambda e: abrir_login(),
                style=ft.ButtonStyle(color="white")
                    ),  

                
                
                
                ft.ElevatedButton(
                    "Registrarse",
                    width=350,
                    height=50,
                    bgcolor="#2563eb",
                    color="white",
                    on_click=registrar_click
                )
                
                

            ],

            expand=True,

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        )

    )