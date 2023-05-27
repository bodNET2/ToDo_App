import flet as ft
import Timer as Ti

def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    clock = Ti.Timer()
    page.add(clock)    
   
ft.app(target=main)
