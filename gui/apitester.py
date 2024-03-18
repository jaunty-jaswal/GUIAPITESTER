import requests
import tkinter as tk
from tkinter import scrolledtext
import threading
import os
from fastapi import FastAPI
import sys
sys.path.append('./')
from routes import routes
import uvicorn
import signal
import subprocess
import contextlib
import io

class Gui:
    
    
    def __init__(self):
        self.info =""
        self.root_ = tk.Tk()
        self.root_.title("apitest")
        self.capture_terminal = io.StringIO()
        self.label_ = tk.Label(self.root_,text="click start")
        self.button_ = tk.Button(self.root_,text="start")
        self.text = scrolledtext.ScrolledText(self.root_, width =80, height=30)
        self.text.grid(row=3)
        self.mainbutton = tk.Button(self.root_,text = "Startapi",command = self.start)
        self.mainbutton.grid(row=3,column=12)
        self.destroy = tk.Button(self.root_,text="close",command=self.closeApi)
        self.destroy.grid(row=3,column=13)
        
        self.root_.mainloop()
        # self.root_.destroy()

    def server(self):
        app = FastAPI()
        app.include_router(routes.router)
        with open('logs.txt','a+') as f:
           with contextlib.redirect_stdout(f):
              uvicorn.run(app=app,host="127.0.0.1",port=8000)
        
             
    def capture_Out(self):
        with open("logs.txt","r+")as f:
            f.seek(0,2)
            while True:
                lines = f.readline()
                self.text.insert(tk.END,lines)


    def start(self):
        thread1 = threading.Thread(target=self.server)
        thread2 = threading.Thread(target=self.start_Api)
        thread3 = threading.Thread(target=self.capture_Out)
        
        thread1.start()
        thread2.start()
        thread3.start()
        
  
    def closeApi(self):
       with open('logs.txt',"w+") as f:
           f.flush()
       os.kill(os.getpid(),signal.SIGTERM)

    def start_Api(self):
       
        self.root = tk.Tk()
        self.root.title("Response")
        self.label = tk.Label(self.root,text="response will be shown here")
        self.label.grid(row=0,column=9)

        self.label1 = tk.Label(self.root,text="name")
        self.label1.grid(row=1,column=8)
        self.entry1 = tk.Entry(self.root,width=20)
        self.entry1.grid(row=1,column=9)
        
        self.label2 = tk.Label(self.root,text="age")
        self.label2.grid(row=2, column = 8)
        self.entry2 = tk.Entry(self.root,width=20)
        self.entry2.grid(row=2,column =9)
        
        
        self.button1 = tk.Button(self.root,text="get",command=self.get_Response,width=1)
        self.button1.grid(row=3,column=9)

        self.button2 = tk.Button(self.root,text="update",command=self.add_Data_Response)
        self.button2.grid(row=3,column=8,sticky="we")
            
        
        self.button3 = tk.Button(self.root, text="delete",command=self.delete_Response,width=3)
        self.button3.grid(row=3,column=10)   

        self.button4 = tk.Button(self.root,text="add",command=self.add_Data)
        self.button4.grid(row=3, column=11)

       

        self.root.mainloop()
       

    def get_Test(self):
        try:
            response = requests.get('http://127.0.0.1:8000/showdata')
            return response.text
        except:
            response = "empty"
            return response    
    def get_Response(self):
        self.label.config(text=self.get_Test())
    
    
    def add_Data(self):
        payload = {"name":self.entry1.get(),"age":self.entry2.get()}
        try:
            response = requests.post('http://127.0.0.1:8000/postdata',json=payload)
            self.label.config(text = response)
        except:
            self.label.config(text="Error!")

    
    def add_Data_Response(self):
        payload = {"name":self.entry1.get(),"age":int(self.entry2.get())}
        try:
            var = requests.put('http://127.0.0.1:8000/update',json=payload)
            self.label.config(text=var)
        except:
            self.label.config(text="error")
    def delete_Response(self):
        payload = {"name":self.entry1.get()}
        try:
            rsponse = requests.delete('http://127.0.0.1:8000/deleteuser',json=payload)
            self.label.config(text=rsponse)
        except:
            self.label.config(text="Error!")

    def display_output(self):
        rout = subprocess.run(['ls','-l'],capture_output=True,text=True)
        self.text.delete("1.0","end")
        self.text.insert("end",rout.stdout)
    def disp(self):
        print("printing value---")
        print(self.capture_terminal)



if __name__ == "__main__":
    ob = Gui()






