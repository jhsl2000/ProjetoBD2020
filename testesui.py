import sys
if sys.version_info[0] < 3:
    import Tkinter as tk     ## Python 2.x
else:
    import tkinter as tk     ## Python 3.x

class LoginPage():
   def __init__(self):
      self.root=tk.Tk()
      label = tk.Label(self.root, text="Welcome to VISA Login Page",fg="blue")
      label.grid(row=0)

      label_1 = tk.Label(self.root, text="Username")
      label_2 = tk.Label(self.root, text="Password")
      self.entry_1 = tk.Entry(self.root)
      self.entry_2 = tk.Entry(self.root, show="*")
      label_1.grid(row=1, sticky="e")
      label_2.grid(row=2, sticky="e")
      self.entry_1.grid(row=1, column=1)
      self.entry_2.grid(row=2, column=1)

      ## doesn't do anything at this time
      ##checkbox = tk.Checkbutton(self.root, text="Keep me logged in")
      ##checkbox.grid(row=3, columnspan=2)

      logbtn = tk.Button(self.root, text="Login", command = self._login_btn_clickked)
      logbtn.grid(row=9, columnspan=2)
      myButton = tk.Button(self.root, text="Exit",command = self.buttonPushed)
      myButton.grid(row=10)

      self.root.mainloop()

   def buttonPushed(self):
      self.root.destroy()

   def _login_btn_clickked(self):
      #print("Clicked")
      username = self.entry_1.get()
      password = self.entry_2.get()

      #print(username, password)

      if username == "test" and password == "test":
          print("OK login")
          #box.showinfo("Login info", "Welcome Tester")
          #button1 = ttk.Button(self.root, text="Please click, Welcome to login!!!",
          #           command=lambda: self.controller.show_frame(StartPage))
          #button1.pack()
      else:
          #box.showerror("Login failed", "Incorrect username")
          print ("Error")

LP=LoginPage()