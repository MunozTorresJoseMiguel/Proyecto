import flet as ft


def LoginView(page, auth_controller):

    page.bgcolor = "#0f172a"

    email_input = ft.TextField(
        label="Correo electrónico",
        width=320,
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
        width=320,
        border_radius=12,
        filled=True,
        bgcolor="#1e293b",
        color="white",
        border_color="#3b82f6"
    )

    def login_click(e):

        user, msg = auth_controller.login(
            email_input.value,
            pass_input.value
        )

        if user:
            page.clean()
            page.add(
                ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, -1),
                        end=ft.Alignment(1, 1),
                        colors=["#0f172a", "#1d4ed8"]
                    ),
                    content=ft.Column(
                        [
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE,
                                size=100,
                                color="white"
                            ),
                            ft.Text(
                                "Bienvenido a JuarezGo",
                                size=35,
                                weight="bold",
                                color="white"
                            ),
                            ft.Text(
                                f"Bienvenido {user['nombre']}",
                                color="white70",
                                size=18
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            )
            page.update()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text(msg)
            )
            page.snack_bar.open = True
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
                ft.Container(height=40),

                ft.Icon(
                    ft.Icons.DIRECTIONS_BUS,
                    size=90,
                    color="white"
                ),
                ft.Text(
                    "JuarezGO",
                    size=38,
                    weight="bold",
                    color="white"
                ),
                ft.Text(
                    "Muévete fácil por Ciudad Juárez",
                    color="white70",
                    size=16
                ),
                ft.Container(height=30),
                email_input,
                pass_input,
                ft.Container(height=10),
                ft.ElevatedButton(
                    "Iniciar Sesión",
                    width=320,
                    height=50,
                    bgcolor="#2563eb",
                    color="white",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=12
                        )
                    ),
                    on_click=login_click
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )