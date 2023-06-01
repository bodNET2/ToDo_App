import time
import tinput as tin
import ctypes
import threading
import flet as ft

def string_parse(stri):
    out = (ctypes.c_int * 3)(0,0,0)
    tin.time_parse(out, stri.encode())
    return list(out)
    # arg = str.split(" ")
    # h = 0
    # m = 0
    # s = 0 

    # for a in range(1, len(arg), 2):
    #    if ( arg[a-1].isnumeric() ):
            
    #        if (arg[a] == "h"):
    #            h = int( arg[a-1] )
    #        elif (arg[a] == "m"):
    #            m = int( arg[a-1] )
    #        elif (arg[a] == "s"):
    #            s = int( arg[a-1] )
    #        else:
    #            print("Missing or incorrect arguments")
    #    else:
    #        return
    
    # return (h,m,s)
       


class Timer(ft.UserControl):
    def __init__(self, full_time=[0,0,0]):
        # cur_time[0]: hours
        # cur_time[1]: minutes
        # cur_time[2]: seconds
        super().__init__()
        self.cur_time = [0,0,0]
        self.running = False
        self.th = None
        self.clock = ft.Text(size = 20)
        self.input_container = ft.Container()

        if (full_time == 0):
            self.full_time = 0
        else:
            self.full_time = full_time

    
    def set_time(self, stri):
        output = string_parse(stri)
       
        new_ti = self.__calculate(output)

        self.cur_time = new_ti
        self.full_time = new_ti
        
        return

    def add_time(self, stri):
        output = string_parse(stri)
        v = []
        w = []

        v = [sum(i) for i in zip(self.cur_time, output)]
        w = [sum(n) for n in zip(self.full_time, output)]
        

        self.cur_time = self.__calculate(v)
        self.full_time = self.__calculate(w)

        return
    
    
    def __calculate(self, ti):
        
        output = [0,0,0]

        if (len(ti) == 3):
            # min_n_sec[0]: minutes
            # min_n_sec[1]: seconds
            mins, sec = divmod(ti[2], 60) 
            ti[2] = sec
            ti[1] += mins 
        
            # hr_n_min[0]: hours
            # hr_n_min[1]: minutes
            hrs, mins = divmod(ti[1], 60)
            ti[1] = mins
            ti[0] += hrs 

            output = ti

        return output

    def display_time(self):
        format_time = "{:02d}:{:02d}:{:02d}".format(self.cur_time[0], 
            self.cur_time[1], self.cur_time[2])
 
        return format_time
        # print(dis_str, end="\r")
    
    
    def start_countdown(self, e):
        self.th = threading.Thread(target = self.countdown, args= (e,), daemon=True)
        self.th.start()
    
    def will_unmount(self):
        self.pause()

    
    def countdown(self, e):
        time_in_sec = (self.cur_time[0]*3600) + (self.cur_time[1]*60) + self.cur_time[2]
        self.running = True
        
        while(self.running and time_in_sec > -1):
            self.cur_time[0] = time_in_sec // 3600
            self.cur_time[1] = (time_in_sec // 60) % 60 
            self.cur_time[2] = time_in_sec % 60

            self.clock.value = self.display_time()
            self.update()
            time.sleep(1)
            time_in_sec -= 1
        
        self.running = False

        return
    
    def pause(self, e):   
        self.running = False
        return

    def clear_time(self, e):
        self.cur_time = [0,0,0]
        self.full_time = [0,0,0]
        self.clock.value = self.display_time()
        self.update()
        
        return
        

    def open_input(self, e):
        self.input_container.content = ft.TextField(hint_text = "Enter a time", on_submit = self.close_input)
        self.input_container.disabled = False
        self.input_container.visible = True
        self.clock.visible = False
        self.update()

    def close_input(self, e):
        if(self.cur_time == [0,0,0] ) and (self.full_time == [0,0,0]):
            self.set_time(self.input_container.content.value) 
        else:
            self.add_time(self.input_container.content.value)
        self.input_container.visible = False
        self.input_container.disabled = True
        self.clock.visible = True
        self.clock.value = self.display_time()
        self.update()

    def build(self):
        #self.input = ft.TextField(hint_text = "Enter a time")
        self.clock.value = self.display_time() 
        
        r1 = ft.Row(controls = [
            #self.new_time_view,
            self.clock, 
            self.input_container,
            ft.IconButton(
                icon=ft.icons.PAUSE,
                icon_color="blue400",
                icon_size= 30,
                tooltip = "Pause clock",
                on_click=self.pause
            ),
            ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color="blue400",
                icon_size= 30,
                tooltip = "Resume clock",
                on_click = self.start_countdown
            ),
            ft.IconButton(
                icon=ft.icons.MORE_TIME,
                icon_color="blue400",
                icon_size= 30,
                tooltip = "Add time",
                on_click = self.open_input
            ),
            ft.IconButton(
                icon=ft.icons.CLEAR,
                icon_color = "blue400",
                icon_size=30,
                tooltip= "Clear time",
                on_click = self.clear_time
            )
        ])

        
        buttons = ft.Container(content = r1, alignment=ft.alignment.center_right) 
        return buttons



"""    
foo = Timer()
s = input("Enter a string in the following format: {} h {} m {} s: ")
foo.set_time(s)
#foo.display_time()

t = input("Enter a string in the following format: {} h {} m {} s: ")
foo.add_time(t)
foo.display_time()

foo.mount()
foo.countdown()
time.sleep(30)
foo.pause()
print(foo.cur_time)
print(foo.full_time)
"""

#foo.display_time()

#t = input("Enter a string in the following format: {} h {} m {} s: ")
#foo.set_time(s, "a")
#foo.display_time()

#start = time.time()
#tin.time_input(s)
#end = time.time()
#print(end-start)

#start1 = time.time()
#string_parse(s)
#end1 = time.time()
#print(end1-start1)