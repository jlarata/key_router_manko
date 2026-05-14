import json
import os
from tkinter import *
from tkinter import ttk
from pynput import keyboard, mouse


map_key_1 = 'u'
map_key_2 = '-'
map_key_3 = '-'
map_key_4 = '-'
map_key_5 = '-'


class key_router:

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                data = json.load(f)
                self.map1.set(data.get("map1", ""))
                self.sat1.set(data.get("map1", "...")) # Sync the label too
                self.key2.set(data.get("key2", ""))
                self.map2.set(data.get("map2", ""))
                self.sat2.set(data.get("map2", "")) 
                self.key3.set(data.get("key3", ""))
                self.map3.set(data.get("map3", ""))
                self.sat3.set(data.get("map3", "")) 
                self.key4.set(data.get("key4", ""))
                self.map4.set(data.get("map4", ""))
                self.sat4.set(data.get("map4", "")) 
                self.key5.set(data.get("key5", ""))
                self.map5.set(data.get("map5", ""))
                self.sat5.set(data.get("map5", "")) 
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
        }
        with open("settings.json", "w") as f:
            json.dump(data, f)
        print("Settings saved!")

    def __init__(self, root):
        
        self.is_simulating = False
        self.is_suspended = False 

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
        ttk.Label(toframe, text="to...", font=("Arial", 10)).grid(column=1, row=2)
        ttk.Label(toframe, text="to...", font=("Arial", 10)).grid(column=1, row=3)
        ttk.Label(toframe, text="to...", font=("Arial", 10)).grid(column=1, row=4)
        ttk.Label(toframe, text="to...", font=("Arial", 10)).grid(column=1, row=5)
        
        self.map1 = StringVar()
        map1_entry = ttk.Entry(mapframe, width=4, textvariable=self.map1, validate='key', validatecommand=vcmd)
        map1_entry.grid(column=1, row=1, sticky=(W, E))

        self.map2 = StringVar()
        map2_entry = ttk.Entry(mapframe, width=4, textvariable=self.map2, validate='key', validatecommand=vcmd)
        map2_entry.grid(column=1, row=2, sticky=(W, E))

        self.map3 = StringVar()
        map3_entry = ttk.Entry(mapframe, width=4, textvariable=self.map3, validate='key', validatecommand=vcmd)
        map3_entry.grid(column=1, row=3, sticky=(W, E))

        self.map4 = StringVar()
        map4_entry = ttk.Entry(mapframe, width=4, textvariable=self.map4, validate='key', validatecommand=vcmd)
        map4_entry.grid(column=1, row=4, sticky=(W, E))

        self.map5 = StringVar()
        map5_entry = ttk.Entry(mapframe, width=4, textvariable=self.map5, validate='key', validatecommand=vcmd)
        map5_entry.grid(column=1, row=5, sticky=(W, E))

        self.sat1 = StringVar(value="-")
        self.sat_label_1 = ttk.Label(satframe, textvariable=self.sat1, font=("Arial", 20)).grid(column=1, row=1)
        self.sat2 = StringVar(value="-")
        self.sat_label_2 = ttk.Label(satframe, textvariable=self.sat2, font=("Arial", 20)).grid(column=1, row=2)
        self.sat3 = StringVar(value="-")
        self.sat_label_3 = ttk.Label(satframe, textvariable=self.sat3, font=("Arial", 20)).grid(column=1, row=3)
        self.sat4 = StringVar(value="-")
        self.sat_label_4 = ttk.Label(satframe, textvariable=self.sat4, font=("Arial", 20)).grid(column=1, row=4)
        self.sat5 = StringVar(value="-")
        self.sat_label_5 = ttk.Label(satframe, textvariable=self.sat5, font=("Arial", 20)).grid(column=1, row=5)
        
        ttk.Button(setframe, text="Set", command = lambda : self.set_key(1)).grid(column=1, row=1)
        ttk.Button(setframe, text="Set", command = lambda : self.set_key(2)).grid(column=1, row=2)
        ttk.Button(setframe, text="Set", command = lambda : self.set_key(3)).grid(column=1, row=3)
        ttk.Button(setframe, text="Set", command = lambda : self.set_key(4)).grid(column=1, row=4)
        ttk.Button(setframe, text="Set", command = lambda : self.set_key(5)).grid(column=1, row=5)

        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(1)).grid(column=1, row=1)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(2)).grid(column=1, row=2)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(3)).grid(column=1, row=3)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(4)).grid(column=1, row=4)
        ttk.Button(resetframe, text="reset", command = lambda : self.reset_key(5)).grid(column=1, row=5)


        self.rows = [
    (self.key2, self.sat2),
    (self.key3, self.sat3),
    (self.key4, self.sat4),
    (self.key5, self.sat5)
]

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
        
    def calculate(self, *args):
        try:
            print("set!")
            """ value = float(self.feet.get())
            self.meters.set(round(0.3048 * value, 4)) """
        except ValueError:
            pass
    
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
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 2:
            try:
                map_key_2 = ""
                self.key2.set("")
                self.sat2.set("")
                self.map2.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 3:
            try:
                map_key_3 = ""
                self.key3.set("")
                self.sat3.set("")
                self.map3.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 4:
            try:
                map_key_4 = ""
                self.key4.set("")
                self.sat4.set("")
                self.map4.set("")
            except Exception as e:
                print(f"Error: {e}")
        if row_number == 5:
            try:
                map_key_5 = ""
                self.key5.set("")
                self.sat5.set("")
                self.map5.set("")
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
        for trigger_var, action_var in app.rows:
            trigger = trigger_var.get()
            action = action_var.get()
            if trigger and action and key.char == trigger:
                app.is_simulating = True
                keyboard_controller.press(action)
                keyboard_controller.release(action)
                app.is_simulating = False
                break
    except AttributeError:
        # Handle special keys (like Ctrl, Alt) here if needed
        pass

def on_click(x, y, button, pressed):
    # 'pressed' is True when clicked down, False when released
    # We only want to trigger the key once per click (on press)
    if pressed and not app.is_suspended:
        
        # Check for a specific button, e.g., Left Click or Middle Click
        if button == mouse.Button.right:
            app.is_simulating = True            
            if map_key_1 != "":
                keyboard_controller.press(map_key_1)
                keyboard_controller.release(map_key_1)
                print(f"Left Click detected at ({x}, {y}) -> Simulating '{map_key_1}' key")
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




