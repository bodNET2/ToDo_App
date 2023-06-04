
import flet as ft
import task as tk
import status as st

class TaskUI(ft.UserControl):
   def __init__(self, padding = 0):
       super().__init__()
       self.space = padding
       self.tasks = ft.Column()
       
       self.filter = ft.Tabs(
           selected_index= 0,
           scale=1.3,
           on_change=self.tab_changed,
           tabs=[
               ft.Tab(text="all"), 
               ft.Tab(text="active"), 
               ft.Tab(text="complete")
            ] 
       )

  
   def build(self):
        self.cov = ft.TextField(hint_text= "What To Do?", expand=True)
        self.items_left = ft.Text()
        self.title = ft.Row(
            controls = [ 
                ft.Text(value="ToDo List", style="headlineMedium", size=40)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.addTaskUI = ft.Row(
            controls = [ 
                self.cov,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=self.add_clicked
                )
            ]
        )

        self.footer = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls= [
                self.items_left,
                ft.OutlinedButton(
                    text="Clear completed",
                    on_click=self.clear_clicked
                )
            ]
        )

        self.subTaskUI = ft.Column(
            width = 800,
            controls = [
                self.title,
                self.addTaskUI,
                self.filter,
                self.tasks,
                self.footer
            ]
        )
        
        return self.subTaskUI  
        """
        return ft.Container(
            width=600,
            #alignment=ft.CrossAxisAlignment.END,
            padding=ft.padding.only(left=self.space),
            #bgcolor=ft.colors.CYAN_200,
            content= self.subTaskUI
        )
        """
        
   def task_delete(self, task):
       self.tasks.controls.remove(task)
       self.update()
   
   def add_clicked(self, e):
       self.tasks.controls.append(tk.Task(self.cov.value, self.task_delete))
       #print("added task")
        #else:
        #    self.subTaskUI.controls.append(tk.Task(self.cov.value, main = False))
       self.cov.value = ""
       #print("clear text field")
       self.update()
    

   def update(self):
       count = 0
       status = self.filter.tabs[self.filter.selected_index].text
       for task in self.tasks.controls:
           task.visible = (status == "all" or 
                           (status == "active" and task.status == st.Status.IN_PROGRESS) or
                           (status == "complete" and task.status == st.Status.COMPLETE))
           #print(task.visible)
           if (task.status != st.Status.COMPLETE):
               count += 1

       self.items_left.value = f"{count} active task(s) left"
       super().update()
           
   def tab_changed(self, e):
       self.update()   

   def clear_clicked(self, e):
       for task in self.tasks.controls[:]:
           if (task.status == st.Status.COMPLETE):
               self.task_delete(task)
       
       self.update()

"""           
def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TaskUI() 
    page.add(todo)    
   
ft.app(target=main)
"""