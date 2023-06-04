import flet as ft
import taskui as tkui

def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = tkui.TaskUI()
    page.add(todo)    
   
ft.app(target=main)
