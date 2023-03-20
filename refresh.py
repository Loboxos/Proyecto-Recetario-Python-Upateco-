import tkinter as tk
import time

class StartPage(tk.Frame):   
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text='EPL Predictions')
        self.label.grid(row=0) 
        
        NG = tk.Button(self, text='New Game',width = 15 ) 
        NG.grid(row=1)
        
        Upcoming = tk.Button(self, text='Upcoming Fixtures', width = 15)
        Upcoming.grid(row=2)
        
        OP = tk.Button(self, text='Odds Progression', width = 15) 
        OP.grid(row=3)
        
        refresh = tk.Button(self, text='Refresh', width = 15, command=lambda: self.refresh_data()) 
        refresh.grid(row=4)

    def update_time(self, time_elapsed):
        self.label.config("text"=time_elapsed)

    def refresh_data(self):
        check_time = time.time()
        for i in range(10):
            time_elapsed = time.time()-check_time
            self.update_time(time_elapsed)
            self.label.update()