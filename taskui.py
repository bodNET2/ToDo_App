
import flet as ft

class TaskUI(ft.UserControl):
   
   
   def build(self):
        self.cov = ft.TextField(hint_text= "Enter a subtask")
        
        self.addTaskUI = ft.Row(
            controls = [ 
                self.cov,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=self.add_clicked
                )
            ]
        )

        self.subTaskUI = ft.Column(
            controls = [
                self.addTaskUI,
            ]
        )
        
            
        return ft.Container(
            content= self.subTaskUI
        )
   
   def add_clicked(self, e):
        self.subTaskUI.controls.append(ft.Checkbox(label = self.cov.value))
        self.cov.value = ""
        self.update()
    


           
def main(page: ft.Page):
    page.title = "ToDo App"
    page.update()

    todo = TaskUI() 
    page.add(todo)    
   
ft.app(target=main)