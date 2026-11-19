import flet as ft
import httpx

API_URL = "https://josh-backend-hto1.onrender.com/name"


def main(page: ft.Page):
    page.title = "josh"
    result = ft.Text("Press the button", size=30)

    def load_name(e):
        result.value = "Loading... (the first request can take a minute)"
        page.update()
        try:
            response = httpx.get(API_URL, timeout=90)
            result.value = response.json()["name"]
        except Exception as error:
            result.value = f"Error: {error}"
        page.update()

    page.add(
        result,
        ft.Button("Get name from back end", on_click=load_name),
    )


ft.run(main)