# https://flet.dev/

import flet as ft
import flet as ft
from exemplo_sem import main as main_sem

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb5.value}'."

        main_sem(model_text=str(tb5.value.replace(" ", "\n")))
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb5 = ft.TextField(
        label="Informe o modelo",
        icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb5, b, t)

ft.app(target=main)