from tkinter import *
from tkinter import ttk
from pynput import keyboard, mouse


map_key_1 = 'u'

class key_router:

    def __init__(self, root):

        root.title("manko_key-router")

        

        mainframe = ttk.Frame(root, padding=(10, 10, 10, 3))
        mainframe.grid(column=0, row=0)

        titleframe = ttk.Frame(mainframe, padding=(10, 10, 10, 10))
        titleframe.grid(column=1, row=2, columnspan=4)

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


        titulo = ttk.Label(titleframe, text="manko_key-router", font=("Arial", 25, "bold"))
        titulo.grid(row=0, column=0, rowspan=4, sticky="we")

        """ self.key1 = StringVar()
        key1_entry = ttk.Entry(keysframe, width=4, textvariable=self.key1)
        key1_entry.grid(column=1, row=1, sticky=(W, E)) """
        ttk.Label(keysframe, text="right click mouse", font=("Arial", 10)).grid(column=1, row=1)

        self.key2 = StringVar()
        key2_entry = ttk.Entry(keysframe, width=4, textvariable=self.key2)
        key2_entry.grid(column=1, row=2, sticky=(W, E))

        self.key3 = StringVar()
        key3_entry = ttk.Entry(keysframe, width=4, textvariable=self.key3)
        key3_entry.grid(column=1, row=3, sticky=(W, E))

        self.key4 = StringVar()
        key4_entry = ttk.Entry(keysframe, width=4, textvariable=self.key4)
        key4_entry.grid(column=1, row=4, sticky=(W, E))

        self.key5 = StringVar()
        key5_entry = ttk.Entry(keysframe, width=4, textvariable=self.key5)
        key5_entry.grid(column=1, row=5, sticky=(W, E))       


        ttk.Label(toframe, text="set to...", font=("Arial", 10)).grid(column=1, row=1)
        ttk.Label(toframe, text="to...", font=("Arial", 20)).grid(column=1, row=2)
        ttk.Label(toframe, text="to...", font=("Arial", 20)).grid(column=1, row=3)
        ttk.Label(toframe, text="to...", font=("Arial", 20)).grid(column=1, row=4)
        ttk.Label(toframe, text="to...", font=("Arial", 20)).grid(column=1, row=5)
        
        self.map1 = StringVar()
        map1_entry = ttk.Entry(mapframe, width=4, textvariable=self.map1)
        map1_entry.grid(column=1, row=1, sticky=(W, E))

        self.map2 = StringVar()
        map2_entry = ttk.Entry(mapframe, width=4, textvariable=self.map2)
        map2_entry.grid(column=1, row=2, sticky=(W, E))

        self.map3 = StringVar()
        map3_entry = ttk.Entry(mapframe, width=4, textvariable=self.map3)
        map3_entry.grid(column=1, row=3, sticky=(W, E))

        self.map4 = StringVar()
        map4_entry = ttk.Entry(mapframe, width=4, textvariable=self.map4)
        map4_entry.grid(column=1, row=4, sticky=(W, E))

        self.map5 = StringVar()
        map5_entry = ttk.Entry(mapframe, width=4, textvariable=self.map5)
        map5_entry.grid(column=1, row=5, sticky=(W, E))


        """ ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=1) """
        asd = ttk.Button(setframe, text="set?", command=self.buttonpressed1).grid(column=1, row=1)
        
        ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=2)
        ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=3)
        ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=4)
        ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=5)
        


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

        """ feet_entry.focus() """

        """ root.bind("<Return>", self.calculate) """
        
    def calculate(self, *args):
        try:
            print("set!")
            """ value = float(self.feet.get())
            self.meters.set(round(0.3048 * value, 4)) """
        except ValueError:
            pass
    
    def buttonpressed1(self, *args):
        global map_key_1
        try:
            value = self.map1.get() # get the first map input text
            if value:
                map_key_1 = value
            else:
                print("Empty text field.")
        except Exception as e:
            print(f"Error: {e}")

def on_press(key):
    try:
        # Check if the pressed key is 'm'
        if key.char == 'm':
            print("Key 'm' pressed: Simulatinmg Left Click")
            mouse_controller.click(mouse.Button.left, 1)
    except AttributeError:
        # Handle special keys (like Ctrl, Alt) here if needed
        pass

def on_click(x, y, button, pressed):
    # 'pressed' is True when clicked down, False when released
    # We only want to trigger the key once per click (on press)
    if pressed:
        
        # Check for a specific button, e.g., Left Click or Middle Click
        if button == mouse.Button.right:
            print(f"Left Click detected at ({x}, {y}) -> Simulating '{map_key_1}' key")
            
            # Press and release the 'a' key
            keyboard_controller.press(map_key_1)
            keyboard_controller.release(map_key_1)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()
mlistener = mouse.Listener(on_click=on_click)
mlistener.start()
klistener = keyboard.Listener(on_press=on_press)
klistener.start()

root = Tk()
key_router(root)
root.mainloop()




