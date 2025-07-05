# main.py

import flet as ft
from elements import header, hero_section, benefits_section, video_section, testimonials_section, footer

def main(page: ft.Page):
    page.title = "Landing Page Nutri"
    page.scroll = ft.ScrollMode.AUTO

    def on_cta_click(e):
        print("CTA clicado - aqui você pode abrir link de pagamento ou form!")

    page.add(
        header(on_cta_click),
        hero_section(on_cta_click),
        benefits_section(),
        video_section(),
        testimonials_section(),
        footer()
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
