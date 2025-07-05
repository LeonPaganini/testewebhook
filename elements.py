# elements.py

import flet as ft
from content import *

def header(on_cta_click):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("APP NUTRI", size=20, weight=ft.FontWeight.BOLD, color=DARK_TEXT),
                ft.ElevatedButton(
                    "Começar Agora",
                    bgcolor=PRIMARY_GREEN,
                    color=WHITE,
                    on_click=on_cta_click
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor=WHITE,
        padding=ft.padding.symmetric(horizontal=20, vertical=12)
    )

def hero_section(on_cta_click):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(HERO_TITLE, size=32, weight=ft.FontWeight.BOLD, color=DARK_TEXT),
                ft.Text(HERO_SUBTITLE, size=16, color=LIGHT_GREEN),
                ft.Image(src=HERO_IMAGE, height=250, fit=ft.ImageFit.COVER),
                ft.ElevatedButton("Quero meu plano", bgcolor=PRIMARY_GREEN, color=WHITE, on_click=on_cta_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        bgcolor=VERY_LIGHT_GREEN,
        padding=ft.padding.all(30)
    )

def benefits_section():
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Icon(getattr(ft.Icons, b["icon"]), color=PRIMARY_GREEN, size=40),
                        ft.Text(b["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT),
                        ft.Text(b["desc"], color=LIGHT_GREEN)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8
                )
                for b in BENEFITS
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        bgcolor=WHITE,
        padding=ft.padding.all(30)
    )

def video_section():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Pronto para começar?", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_GREEN),
                ft.WebView(url=VIDEO_URL, height=300)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        bgcolor=VERY_LIGHT_GREEN,
        padding=ft.padding.all(30)
    )

def testimonials_section():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(src=t["img"], width=80, height=80, border_radius=40),
                        ft.Column(
                            controls=[
                                ft.Text(t["text"], italic=True, color=DARK_TEXT),
                                ft.Text(t["author"], size=12, color=LIGHT_GREEN)
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=12
                )
                for t in TESTIMONIALS
            ],
            spacing=20
        ),
        bgcolor=WHITE,
        padding=ft.padding.all(30)
    )

def footer():
    return ft.Container(
        content=ft.Text("©️ 2024 Todos os direitos reservados - APP NUTRI", size=12, color=LIGHT_GREEN),
        bgcolor=WHITE,
        padding=ft.padding.all(20)
    )
