import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox

db = "Student.db"

class StudentManager:
    
    def init_db(self):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
    
        cur.execute("""
        CREATE TABLE IF NOT EXISTS studentdata(
            id INTEGER PRIMARY KEY,
            name TEXT,
            task TEXT,
            due TEXT
    )
    """)
        conn.commit()
        conn.close()
        
#  FUNCTIONS
    
    def add_student(self):
        name = simpledialog.askstring("StudentName","Your Name:")
        task = simpledialog.askstring("StudentTask","Enter Your Task:")
        due = simpledialog.askstring("Due_Date","Enter Due Date:")
        
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        
        cur.execute("INSERT INTO studentdata(name, task, due) VALUES(?, ?, ?)",
                    (name, task, due))
        conn.commit()
        conn.close()
        
    def view_student(self):
        
        conn=sqlite3.connect(db)
        cur = conn.cursor()
        
        cur.execute("SELECT id, name, task, due FROM studentdata")
        rows = cur.fetchall()
        
        if not rows:
            messagebox.showerror("StudentData","No Data Yet!")
            return 
        
        text =""
        for r in rows:
            text += (f"{r[0]}.{r[1]}-{r[2]}-{r[3]}")
        
        messagebox.showinfo("STudentData",text)
        
    def dlt_task(self):
        
        studentdata_id = simpledialog.askstring("DELETE","Enter ID you want to delete:")
        
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        
        cur.execute("DELETE FROM studentdata WHERE ID =?",(studentdata_id))
        if not studentdata_id:
            messagebox.showerror("Error","No studnet id availabe")
            return        
        conn.commit()
        conn.close()
        
        
        messagebox.showinfo("Task","Delete successfully")
        
        
        
Student = StudentManager()
Student.init_db()

#  GUI

root = tk.Tk()
root.title("SUkha's Student Manageer")
root.geometry("350x350")

label = tk.Label(root,text="Studnet Manager",font=("Arial",16))
label.pack(pady=20)

btn_add = tk.Button(root,text="Add Studnet",width=25,command=Student.add_student)
btn_add.pack(pady=5)

btn_view = tk.Button(root,text="View Data",width=25,command=Student.view_student)
btn_view.pack(pady=5)

btn_dlt = tk.Button(root,text="Delete Task",width=25,command=Student.dlt_task)
btn_dlt.pack(pady=5)

root.mainloop()