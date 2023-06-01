import status as st
import flet as ft
import Timer as ti

class Task(ft.UserControl):
    def __init__(self, name=None):
        super().__init__()
        if (name is not None):
            self.name = name
        else:
            self.name = ""
        
        self.description = ft.Markdown(visible=False, disabled=True)
       
        self.notes = ft.TextField(
            hint_text="A notepad for your thoughts", 
            label="Notes",
            multiline=True,
            #on_submit=self.add_description
        )

        self.post_note = ft.Column(
            visible=False,
            disabled=True,
            controls = [
                self.notes,
                ft.FloatingActionButton(
                    text="Submit",
                    width=100,
                    on_click= self.add_description
                )
            ]
        )
        
        
        self.status = st.Status.NOT_STARTED
        self.timer = None
        self.subTasks = []

    
    def add_description(self, e):
        self.post_note.visible=False
        self.post_note.disabled=True

        self.description.value=self.notes.value
        self.description.selectable=True
        self.description.visible=True
        self.description.disabled=False
        self.description.extension_set=ft.MarkdownExtensionSet.GITHUB_WEB
        self.description.code_theme="atom-one-dark"
        #self.description.code_style=ft.TextStyle(font_family="Roboto Mono")
         
        self.update()
    

    def add_subTasks(self, subtask):
        self.subTasks.append(subtask)

    def make_notes_visible(self, e):
        self.post_note.disabled=False
        self.post_note.visible=True

        self.description.visible = False
        
        self.update()

    def start_edit_task(self, e):
        self.display_task.visible = False
        self.edit.disabled = False
        self.edit.visible = True
        self.update()

    def end_edit_task(self, e):
        self.display_task.label = self.edit.value
        self.display_task.visible = True
        self.edit.visible = False
        self.edit.disabled = True  
        self.update()

    def build(self):
        self.display_task = ft.Checkbox(value = False, label = self.name)

        self.edit = ft.TextField(value=self.display_task.label, 
                                 on_submit=self.end_edit_task, visible=False, disabled=True)

        self.pomodoro = ti.Timer()

        task_menu = ft.Row(    
            controls = [
                self.edit,
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_size= 20,
                    tooltip = "Edit task",
                    on_click=self.start_edit_task
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE_ROUNDED,
                    icon_size= 20,
                    tooltip = "Delete task",
                    # on_click=self.pause
                ),
                ft.IconButton(
                    icon=ft.icons.NOTES,
                    icon_size=20,
                    tooltip = "Add Notes",
                    on_click = self.make_notes_visible
                )
            ]
        )

        task_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls = [
                self.display_task,
                task_menu
            ]
        )

        
        # Container
        # |    Column    
        # |    |    Row (TextField + FloatingActionButton) 
        # |    |    Task    
              
        
    

        return ft.Column(
            width = 600,
            controls = [
                task_view,
                self.pomodoro,
                self.post_note,
                self.description 
            ]    
        )
        
    



def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    g = Task("ghorp")
    # clock = Ti.Timer()
    page.add(g)    
   
ft.app(target=main)


