import json
import os
import time
from tkinter import *
from tkinter import ttk, PhotoImage
from pynput import keyboard, mouse
from pynput.keyboard import Key


map_key_1 = 'u'
map_key_2 = '-'
map_key_3 = '-'
map_key_4 = '-'
map_key_5 = '-'
sat1 = ''
sat2 = ''
sat3 = ''
sat4 = ''
sat5 = ''
click_1_coordinates = {'x' : 0, 'y': 0}
click_2_coordinates = {'x' : 0, 'y': 0}
click_3_coordinates = {'x' : 0, 'y': 0}
click_4_coordinates = {'x' : 0, 'y': 0}
click_5_coordinates = {'x' : 0, 'y': 0}
click_currently_mapping = 0

class key_router:

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                data = json.load(f)
                self.map1.set(data.get("map1", ""))
                self.sat1.set(data.get("sat1", "...")) # Sync the label too
                self.click1_x.set(data.get("click_1_coordinates.x", ""))                
                self.click1_y.set(data.get("click_1_coordinates.y", ""))                
                self.key2.set(data.get("key2", ""))
                self.map2.set(data.get("map2", ""))
                self.sat2.set(data.get("sat2", ""))
                self.click2_x.set(data.get("click_2_coordinates.x", ""))
                self.click2_y.set(data.get("click_2_coordinates.y", ""))   
                self.key3.set(data.get("key3", ""))
                self.map3.set(data.get("map3", ""))
                self.sat3.set(data.get("sat3", "")) 
                self.click3_x.set(data.get("click_3_coordinates.x", ""))                
                self.click3_y.set(data.get("click_3_coordinates.y", ""))  
                self.key4.set(data.get("key4", ""))
                self.map4.set(data.get("map4", ""))
                self.sat4.set(data.get("sat4", "")) 
                self.click4_x.set(data.get("click_4_coordinates.x", ""))                
                self.click4_y.set(data.get("click_4_coordinates.y", ""))  
                self.key5.set(data.get("key5", ""))
                self.map5.set(data.get("map5", ""))
                self.sat5.set(data.get("sat5", "")) 
                self.click5_x.set(data.get("click_5_coordinates.x", ""))                
                self.click5_y.set(data.get("click_5_coordinates.y", ""))  
                return data.get("map1", "u") # Return the global mapping value
        return "u" # Default if no file exists
    
    def save_settings(self):
        data = {
            "map1": self.map1.get(),
            "map2": self.map2.get(),
            "map3": self.map3.get(),
            "map4": self.map4.get(),
            "map5": self.map5.get(),

            "key2":self.key2.get(),
            "key3":self.key3.get(),
            "key4":self.key4.get(),
            "key5":self.key5.get(),

            "sat1":self.sat1.get(),
            "sat2":self.sat2.get(),
            "sat3":self.sat3.get(),
            "sat4":self.sat4.get(),
            "sat5":self.sat5.get(),

            "click_1_coordinates.x" : self.click1_x.get(),
            "click_1_coordinates.y" : self.click1_y.get(),
            "click_2_coordinates.x" : self.click2_x.get(),
            "click_2_coordinates.y" : self.click2_y.get(),
            "click_3_coordinates.x" : self.click3_x.get(),
            "click_3_coordinates.y" : self.click3_y.get(),
            "click_4_coordinates.x" : self.click4_x.get(),
            "click_4_coordinates.y" : self.click4_y.get(),
            "click_5_coordinates.x" : self.click5_x.get(),
            "click_5_coordinates.y" : self.click5_y.get(),
        }
        with open("settings.json", "w") as f:
            json.dump(data, f)
        print("Settings saved!")

    def __init__(self, root):
        
        self.is_simulating = False
        self.is_suspended = False 
        self.cursor_image = PhotoImage(file="cursor.png")
        self.is_mapping_click = False
        self.click_buttons = []

        root.title("manko_key-router")
        
        mainframe = ttk.Frame(root, padding=(10, 10, 10, 3))
        mainframe.grid(column=0, row=0)

        titleframe = ttk.Frame(mainframe, padding=(10, 10, 10, 10))
        titleframe.grid(column=1, row=2, columnspan=5)

        keysframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        keysframe.grid(column=1, row=4, sticky=(W, E))
        keysframe.rowconfigure(1, minsize=80)
        keysframe.rowconfigure(2, minsize=80)
        keysframe.rowconfigure(3, minsize=80)
        keysframe.rowconfigure(4, minsize=80)
        keysframe.rowconfigure(5, minsize=80)

        toframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        toframe.grid(column=2, row=4)
        toframe.rowconfigure(1, minsize=80)
        toframe.rowconfigure(2, minsize=80)
        toframe.rowconfigure(3, minsize=80)
        toframe.rowconfigure(4, minsize=80)
        toframe.rowconfigure(5, minsize=80)

        mapframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        mapframe.grid(column=3, row=4, sticky=(W, E))
        mapframe.rowconfigure(1, minsize=80)
        mapframe.rowconfigure(2, minsize=80)
        mapframe.rowconfigure(3, minsize=80)
        mapframe.rowconfigure(4, minsize=80)
        mapframe.rowconfigure(5, minsize=80)

        setframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        setframe.grid(column=4, row=4, sticky=(W, E))
        setframe.rowconfigure(1, minsize=80)
        setframe.rowconfigure(2, minsize=80)
        setframe.rowconfigure(3, minsize=80)
        setframe.rowconfigure(4, minsize=80)
        setframe.rowconfigure(5, minsize=80)

        satframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        satframe.grid(column=5, row=4)
        satframe.rowconfigure(1, minsize=80)
        satframe.rowconfigure(2, minsize=80)
        satframe.rowconfigure(3, minsize=80)
        satframe.rowconfigure(4, minsize=80)
        satframe.rowconfigure(5, minsize=80)

        resetframe = ttk.Frame(mainframe, relief='raised', borderwidth=5, padding=(10, 10, 10, 3))
        resetframe.grid(column=6, row=4, sticky=(W, E))
        resetframe.rowconfigure(1, minsize=80)
        resetframe.rowconfigure(2, minsize=80)
        resetframe.rowconfigure(3, minsize=80)
        resetframe.rowconfigure(4, minsize=80)
        resetframe.rowconfigure(5, minsize=80)

        titulo = ttk.Label(titleframe, text="manko_key-router", font=("Arial", 25, "bold"))
        titulo.grid(row=0, column=0, rowspan=4, sticky="we")

        ttk.Label(mainframe, text="OUTPUT", font=("Arial", 15)).grid(column=5, row=3)

        self.status_var = StringVar(value="Status: Active")
        self.status_label = ttk.Label(titleframe, textvariable=self.status_var, font=("Arial", 10, "italic"), foreground="green")
        self.status_label.grid(row=4, column=1)

        self.status_xplaining = StringVar(value="CTRL+K para suspender o activar")
        self.status_xplaining_lbl = ttk.Label(titleframe, textvariable=self.status_xplaining, font=("Arial", 10, "italic"))
        self.status_xplaining_lbl.grid(row=4, column=0)

        ttk.Label(keysframe, text="right click mouse", font=("Arial", 10)).grid(column=1, row=1)

        self.key2 = StringVar()
        key2_entry = ttk.Entry(keysframe, width=4, textvariable=self.key2, validate='key', validatecommand=vcmd)
        key2_entry.grid(column=1, row=2, sticky=(W, E))

        self.key3 = StringVar()
        key3_entry = ttk.Entry(keysframe, width=4, textvariable=self.key3, validate='key', validatecommand=vcmd)
        key3_entry.grid(column=1, row=3, sticky=(W, E))

        self.key4 = StringVar()
        key4_entry = ttk.Entry(keysframe, width=4, textvariable=self.key4, validate='key', validatecommand=vcmd)
        key4_entry.grid(column=1, row=4, sticky=(W, E))

        self.key5 = StringVar()
        key5_entry = ttk.Entry(keysframe, width=4, textvariable=self.key5, validate='key', validatecommand=vcmd)
        key5_entry.grid(column=1, row=5, sticky=(W, E))       


        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=1)
        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=2)
        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=3)
        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=4)
        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=5)

        
        
        self.map1 = StringVar()
        self.click1_x = StringVar()
        self.click1_y = StringVar()
        self.text1 = StringVar()
        if self.map1 != "":
            self.text1 = self.map1
        else:
            self.text1= f"x: {self.click1_x}, y: {self.click1_x}"

        map1_entry = ttk.Entry(mapframe, width=4, textvariable=self.text1, validate='key', validatecommand=vcmd)
        map1_entry.grid(column=1, row=1, sticky=(W, E))

        self.click1_x = StringVar()
        self.click1_y = StringVar()
        click1 = ttk.Button(mapframe, image=self.cursor_image, command = lambda : self.enable_mapping_click(1))
        click1.grid(column=3, row=1)
        self.click_buttons.append(click1)

        
        self.map2 = StringVar()
        self.click2_x = StringVar()
        self.click2_y = StringVar()
        self.text2 = StringVar()
        if self.map2 != "":
            self.text2 = self.map2
        else:
            self.text2 = f"x: {self.click2_x}, y: {self.click2_x}"
        
        map2_entry = ttk.Entry(mapframe, width=4, textvariable=self.text2, validate='key', validatecommand=vcmd)
        map2_entry.grid(column=1, row=2, sticky=(W, E))

        click2 = ttk.Button(mapframe, image=self.cursor_image, command = lambda : self.enable_mapping_click(2))
        click2.grid(column=3, row=2)
        self.click_buttons.append(click2)


        self.map3 = StringVar()
        self.click3_x = StringVar()
        self.click3_y = StringVar()
        self.text3 = StringVar()
        if self.map3 != "":
            self.text3 = self.map3
        else:
            self.text3 = f"x: {self.click3_x}, y: {self.click3_x}"
        map3_entry = ttk.Entry(mapframe, width=4, textvariable=self.text3, validate='key', validatecommand=vcmd)
        map3_entry.grid(column=1, row=3, sticky=(W, E))

        self.click3_x = StringVar()
        self.click3_y = StringVar()
        click3 = ttk.Button(mapframe, image=self.cursor_image, command = lambda : self.enable_mapping_click(3))
        click3.grid(column=3, row=3)
        self.click_buttons.append(click3)


        self.map4 = StringVar()
        self.click4_x = StringVar()
        self.click4_y = StringVar()
        self.text4 = StringVar()
        if self.map4 != "":
            self.text4 = self.map4
        else:
            self.text4 = f"x: {self.click4_x}, y: {self.click4_x}"
        map4_entry = ttk.Entry(mapframe, width=4, textvariable=self.text4, validate='key', validatecommand=vcmd)
        map4_entry.grid(column=1, row=4, sticky=(W, E))

        self.click4_x = StringVar()
        self.click4_y = StringVar()
        click4 = ttk.Button(mapframe, image=self.cursor_image, command = lambda : self.enable_mapping_click(4))
        click4.grid(column=3, row=4)
        self.click_buttons.append(click4)


        self.map5 = StringVar()
        self.click5_x = StringVar()
        self.click5_y = StringVar()
        self.text5 = StringVar()
        if self.map5 != "":
            self.text5 = self.map5
        else:
            self.text5 = f"x: {self.click5_x}, y: {self.click5_x}"
        map5_entry = ttk.Entry(mapframe, width=4, textvariable=self.text5, validate='key', validatecommand=vcmd)
        map5_entry.grid(column=1, row=5, sticky=(W, E))

        self.click5_x = StringVar()
        self.click5_y = StringVar()
        click5 = ttk.Button(mapframe, image=self.cursor_image, command = lambda : self.enable_mapping_click(5))
        click5.grid(column=3, row=5)
        self.click_buttons.append(click5)

        self.sat1 = StringVar(value="-")
        self.sat_label_1 = ttk.Label(satframe, textvariable=self.sat1, font=("Arial", 15)).grid(column=1, row=1)
        self.sat2 = StringVar(value="-")
        self.sat_label_2 = ttk.Label(satframe, textvariable=self.sat2, font=("Arial", 15)).grid(column=1, row=2)
        self.sat3 = StringVar(value="-")
        self.sat_label_3 = ttk.Label(satframe, textvariable=self.sat3, font=("Arial", 15)).grid(column=1, row=3)
        self.sat4 = StringVar(value="-")
        self.sat_label_4 = ttk.Label(satframe, textvariable=self.sat4, font=("Arial", 15)).grid(column=1, row=4)
        self.sat5 = StringVar(value="-")
        self.sat_label_5 = ttk.Label(satframe, textvariable=self.sat5, font=("Arial", 15)).grid(column=1, row=5)
        
        ttk.Button(setframe, text="Set Key", command = lambda : self.set_key(1)).grid(column=1, row=1)
        ttk.Button(setframe, text="Set Key", command = lambda : self.set_key(2)).grid(column=1, row=2)
        ttk.Button(setframe, text="Set Key", command = lambda : self.set_key(3)).grid(column=1, row=3)
        ttk.Button(setframe, text="Set Key", command = lambda : self.set_key(4)).grid(column=1, row=4)
        ttk.Button(setframe, text="Set Key", command = lambda : self.set_key(5)).grid(column=1, row=5)

        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(1)).grid(column=1, row=1)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(2)).grid(column=1, row=2)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(3)).grid(column=1, row=3)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(4)).grid(column=1, row=4)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(5)).grid(column=1, row=5)


        #################### TRIGGERS AND ACTIONS #################### 
        self.rows = [ (self.key2, self.sat2, self.click2_x, self.click2_y), (self.key3, self.sat3, self.click3_x, self.click3_y), (self.key4, self.sat4, self.click4_x, self.click4_y), (self.key5, self.sat5, self.click5_x, self.click5_y) ]

        saved_key = self.load_settings()
        global map_key_1
        map_key_1 = saved_key

        """ self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
 """
        """ root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1) """

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)
            
        for child in keysframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)

        for child in toframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)    

        for child in mapframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)    

        for child in setframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)
        
        for child in satframe.winfo_children(): 
            child.grid_configure(padx=5, pady=10)

        """ feet_entry.focus() """
        """ root.bind("<Return>", self.calculate) """

    def enable_mapping_click(self, number):
        global click_currently_mapping
        click_currently_mapping = number
        for btn in self.click_buttons:
            btn.config(state="disabled")
        print(f"toggling is_mapping_click from {self.is_mapping_click} to {not self.is_mapping_click}")
        self.is_mapping_click = not self.is_mapping_click
        
    def reset_mapping_buttons(self):
        for btn in self.click_buttons:
            btn.config(state="normal") 

    def set_click(self, x, y, *args):
        global click_1_coordinates, click_2_coordinates, click_3_coordinates, click_4_coordinates, click_5_coordinates, click_currently_mapping, map_key_1, map_key_2, map_key_3, map_key_4, map_key_5
        if click_currently_mapping == 1:
            try:
                map_key_1 = ""
                self.click1_x.set(x)
                self.click1_y.set(y)
                self.sat1.set(f"x: {x}, y: {y}")            
            except Exception as e:
                print(f"Error: {e}")    
        if click_currently_mapping == 2:
            try:
                value = self.key2.get()
                if value:
                    map_key_2 = ""
                    self.click2_x.set(x)
                    self.click2_y.set(y)
                    self.sat2.set(f"x: {x}, y: {y}")
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if click_currently_mapping == 3:
            try:
                value = self.key3.get()
                if value:
                    map_key_3 = ""
                    self.click3_x.set(x)
                    self.click3_y.set(y)
                    self.sat3.set(f"x: {x}, y: {y}")
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if click_currently_mapping == 4:
            try:
                value = self.key4.get()
                if value:
                    map_key_4 = ""
                    self.click4_x.set(x)
                    self.click4_y.set(y)
                    self.sat4.set(f"x: {x}, y: {y}")
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")  
        if click_currently_mapping == 5:
            try:
                value = self.key5.get()
                if value:
                    map_key_5 = ""
                    self.click5_x.set(x)
                    self.click5_y.set(y)
                    self.sat5.set(f"x: {x}, y: {y}")
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")   
        self.save_settings()


    def set_key(self, row_number, *args):
        global map_key_1, map_key_2, map_key_3, map_key_4, map_key_5
        if row_number == 1:
            try:
                value = self.map1.get() # get the first map input text
                if value:
                    map_key_1 = value
                    self.sat1.set(value)
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if row_number == 2:
            try:
                value = self.map2.get()
                if value:
                    map_key_2 = value
                    self.sat2.set(value)
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if row_number == 3:
            try:
                value = self.map3.get()
                if value:
                    map_key_3 = value
                    self.sat3.set(value)
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if row_number == 4:
            try:
                value = self.map4.get()
                if value:
                    map_key_4 = value
                    self.sat4.set(value)
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")    
        if row_number == 5:
            try:
                value = self.map5.get()
                if value:
                    map_key_5 = value
                    self.sat5.set(value)
                else:
                    print("Empty text field.")
            except Exception as e:
                print(f"Error: {e}")
        self.save_settings()
    
    def reset_key(self, row_number, *args):
        global map_key_1, map_key_2, map_key_3, map_key_4, map_key_5
        if row_number == 1:
            try:
                map_key_1 = ""
                self.sat1.set("")
                self.map1.set("")
                self.click1_x.set("")
                self.click1_y.set("")
                self.text1.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 2:
            try:
                map_key_2 = ""
                self.key2.set("")
                self.sat2.set("")
                self.map2.set("")
                self.click2_x.set("")
                self.click2_y.set("")
                self.text2.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 3:
            try:
                map_key_3 = ""
                self.key3.set("")
                self.sat3.set("")
                self.map3.set("")
                self.click3_x.set("")
                self.click3_y.set("")
                self.text3.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 4:
            try:
                map_key_4 = ""
                self.key4.set("")
                self.sat4.set("")
                self.map4.set("")
                self.click4_x.set("")
                self.click4_y.set("")
                self.text4.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 5:
            try:
                map_key_5 = ""
                self.key5.set("")
                self.sat5.set("")
                self.map5.set("")
                self.click5_x.set("")
                self.click5_y.set("")
                self.text5.set("")
            except Exception as e:
                print(f"Error: {e}")
        self.save_settings()

    def toggle_suspension(self):
        """Toggles the state of remapping."""
        self.is_suspended = not self.is_suspended
        if self.is_suspended:
            state = "SUSPENDED"
            color = "red"
        else:
            state = "Active"
            color = "green"        
        self.status_var.set(f"Status: {state}")
        self.status_label.configure(foreground=color)
        print(f"Remapping is now {state}")
    
    

def limit_entry(P):
    # P is the value the entry would have if the change is allowed
    if len(P) <= 1:
        return True
    return False

def on_press(key):
    if app.is_simulating or app.is_suspended:
        return
    try:
        for trigger_var, action_var, x, y in app.rows:
            trigger = trigger_var.get()
            action = action_var.get()
            if trigger and action and key.char == trigger:
                if len(action) == 1:
                    app.is_simulating = True
                    keyboard_controller.press(action)
                    keyboard_controller.release(action)
                    app.is_simulating = False
                    break
                else: 
                    print(f"clicking in {int(x.get())}, {int(y.get())}")
                    mouse_controller.position = (int(app.click1_x.get()), int(app.click1_y.get()))
                    mouse_controller.press(mouse.Button.left)
                    mouse_controller.release(mouse.Button.left)
    except AttributeError:
        # Handle special keys (like Ctrl, Alt) here if needed
        pass



def toggle_mapping_click():
    print(f"toggling app.is_mapping_click from {app.is_mapping_click} to {not app.is_mapping_click}")
    app.is_mapping_click = not app.is_mapping_click
    if not app.is_mapping_click:
        app.reset_mapping_buttons()
    

def on_click(x, y, button, pressed):
    if app.is_simulating:
        return
    if not pressed:
        if app.is_mapping_click:
            if button == mouse.Button.left:
                print(f"left Click detected at ({x}, {y})")
                app.set_click(x, y)
            toggle_mapping_click()
            return

        if not app.is_suspended:       
            if button == mouse.Button.right:
                app.is_simulating = True
                try:
                    if app.sat1.get() != "":
                        if len(app.sat1.get()) == 1:
                            #print("a")
                            keyboard_controller.press(map_key_1)
                            keyboard_controller.release(map_key_1)
                        else:
                            #print("b")
                            mouse_controller.position = (int(app.click1_x.get()), int(app.click1_y.get()))
                            time.sleep(0.01)
                            mouse.Controller.click(mouse.Button.left)
                            #mouse_controller.press(mouse.Button.left)
                            #mouse_controller.release(mouse.Button.left)
                except Exception as e:
                    print(f"error during simulation: {e}")
                finally:
                    time.sleep(0.02)
                    app.is_simulating = False


mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

hotkey_listener = keyboard.GlobalHotKeys({'<ctrl>+k': lambda: app.toggle_suspension()})
hotkey_listener.start()
mlistener = mouse.Listener(on_click=on_click)
mlistener.start()
klistener = keyboard.Listener(on_press=on_press)
klistener.start()

root = Tk()
vcmd = (root.register(limit_entry), '%P')

app = key_router(root)
root.mainloop()




