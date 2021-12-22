from tkinter import * 
from PIL import ImageTk, Image
from send_mail import send_mail

def read_data():
    
    global  input1, input2, input3, password, message

    sender_mail     = input1.get()
    receiver_mail   = input2.get()
    subject         = input3.get()
    spassword       = password.get()
    msg             = message.get("1.0","end-1c")

    response, value = send_mail(sender_mail, spassword, receiver_mail, subject, msg)

    window_x = window.winfo_rootx()
    window_y = window.winfo_rooty()
    winfo_x = window_x + 100
    winfo_y = window_y + 100

    popup = Toplevel()
    popup.geometry(f"300x300+{winfo_x}+{winfo_y}")
    popup.wm_title("Message")
    Label(popup, text= response, font=("Helvetica", 15)).place(x=23,y=110)
    
    popup.wait_visibility()
    popup.grab_set_global()

    b = Button(popup, text="OK", command=exit).grid(row=20, column=15, padx=150, pady=200)
    
    
    


window = Tk()

window.title("Mail sender")
window.configure(width=500, height=600)
window.configure(bg='lightgray')
window.eval('tk::PlaceWindow . center')


#bg = PhotoImage( file = "mail.jpg")
canvas1 = Canvas(window, width=500, height=580, bg='white')
canvas1.pack(fill = "both", expand = True)
img = ImageTk.PhotoImage(Image.open("mail2.jpg"))
 
canvas1.create_image( 0, 0, image = img, anchor = "nw")

text = Label(canvas1, text="Your mail address:", font=("Helvetica", 11))
text.place(x=40,y=30)
input1 = Entry(canvas1, width=26, font=("Helvetica", 11))
input1.place(x=250,y=30)

password_label = Label(canvas1, text="Password:", font=("Helvetica", 11))
password_label.place(x=40,y=70)
password = Entry(canvas1, width=26, show="*", font=("Helvetica", 11))
password.place(x=250,y=70)

text2 = Label(canvas1, text="Receiver mail address:", font=("Helvetica", 11))
text2.place(x=40,y=115)
input2 = Entry(canvas1, width=26, font=("Helvetica", 11))
input2.place(x=250,y=115)

text3 = Label(canvas1, text="Subject:", font=("Helvetica", 11))
text3.place(x=40,y=160)
input3 = Entry(canvas1, width=26, font=("Helvetica", 11))
input3.place(x=250,y=160)

text4 = Label(canvas1, text="Message:", font=("Helvetica", 11))
text4.place(x=40,y=210)
message = Text(canvas1, height = 18, width = 52)
message.place(x=40,y=240)

send = Button(canvas1, text="SEND", width=15, font=("Helvetica", 11), command=read_data)
send.place(x=313,y=540)

window.mainloop()