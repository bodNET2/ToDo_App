import flet as ft
import Timer as Ti

class TodoApp(ft.UserControl):
    def build(self):
        # Initialize a text field element
        self.new_task = ft.TextField(hint_text = "What needs to be done?", expand = True)
        # Lay out child elements in a column
        self.tasks = ft.Column()
        self.clock = Ti.Timer()
        # Main column
        #self.clock.set_time('1m')
        #self.clock.mount()
        #self.clock.countdown()

        return ft.Column(
            width = 600,
            controls = [
                ft.Row(
                    controls = [
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD,
                            on_click=self.add_clicked
                        )
                    ]
                ),
                self.tasks
            ] 
        )
    
    def add_clicked(self, e):
        self.tasks.controls.append(ft.Checkbox(label = self.new_task.value))
        self.new_task.value = ""
        self.update()

    

def main(page: ft.Page):
    page.title = "ToDo App"
    page.update()

    todo = TodoApp() 
    clock = Ti.Timer()
    page.add(todo)    
   
ft.app(target=main)
