from tkinter import *
from tkinter import ttk

class key_router:

    def __init__(self, root):

        root.title("manko_key-router")

        mainframe = ttk.Frame(root, padding=(10, 10, 10, 3))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        titleframe = ttk.Frame(mainframe, padding=(10, 10, 10, 10))
        titleframe.grid(column=2, row=1)

        keysframe = ttk.Frame(mainframe, width=4, padding=(10, 10, 10, 3))
        keysframe.grid(column=1, row=4)

        toframe = ttk.Frame(mainframe, padding=(10, 10, 10, 3))
        toframe.grid(column=2, row=4)

        mapframe = ttk.Frame(mainframe, padding=(10, 10, 10, 3))
        mapframe.grid(column=3, row=4)

        setframe = ttk.Frame(mainframe, padding=(10, 10, 10, 3))
        setframe.grid(column=4, row=4)



        ttk.Label(titleframe, text="manko_key-router").grid(column=3, row=3)

        self.key1 = StringVar()
        key1_entry = ttk.Entry(keysframe, width=4, textvariable=self.key1)
        key1_entry.grid(column=1, row=1, sticky=(W, E))

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


        ttk.Label(toframe, text="to...").grid(column=1, row=1, sticky=W)
        ttk.Label(toframe, text="to...").grid(column=1, row=2, sticky=W)
        ttk.Label(toframe, text="to...").grid(column=1, row=3, sticky=W)
        ttk.Label(toframe, text="to...").grid(column=1, row=4, sticky=W)
        ttk.Label(toframe, text="to...").grid(column=1, row=5, sticky=W)
        
        self.map1 = StringVar()
        map1_entry = ttk.Entry(mapframe, width=1, textvariable=self.map1)
        map1_entry.grid(column=1, row=1, sticky=(W, E))

        self.map2 = StringVar()
        map2_entry = ttk.Entry(mapframe, width=1, textvariable=self.map2)
        map2_entry.grid(column=1, row=2, sticky=(W, E))

        self.map3 = StringVar()
        map3_entry = ttk.Entry(mapframe, width=1, textvariable=self.map3)
        map3_entry.grid(column=1, row=3, sticky=(W, E))

        self.map4 = StringVar()
        map4_entry = ttk.Entry(mapframe, width=1, textvariable=self.map4)
        map4_entry.grid(column=1, row=4, sticky=(W, E))

        self.map5 = StringVar()
        map5_entry = ttk.Entry(mapframe, width=1, textvariable=self.map5)
        map5_entry.grid(column=1, row=5, sticky=(W, E))


        """ ttk.Button(setframe, text="Set!", command=self.calculate).grid(column=1, row=1) """
        asd = ttk.Button(setframe, text="set?", command=self.buttonpressed).grid(column=1, row=1)
        
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
    
    def buttonpressed(self, *args):
        try:
            value = self.key1.get()
            print(str(value))
        except ValueError:
            print(ValueError)

root = Tk()
key_router(root)
root.mainloop()