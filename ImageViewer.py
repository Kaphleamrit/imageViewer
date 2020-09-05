from tkinter import *
from PIL import ImageTk, Image



root = Tk()

root.title("Image viewer")
# root.geometry("500x500")

# image objects
my_img6 = ImageTk.PhotoImage(Image.open("images/img.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/img.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/img6.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("images/img7.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/img8.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("images/img9.jpg"))



# imagesArray
imageList = [ my_img1 , my_img2 , my_img3 , my_img4 , my_img5, my_img6 ,my_img7, my_img8, my_img9  , my_img10 ]
counter = 0;


# triggers when back button is pressed
def back():
     global my_label,counter,button_back,button_forward,status
     counter = counter -1

     button_back = Button(root, text="<<", command = back)
     button_back.grid(row =1 , column = 0)

     # if start of the array is reached the back button is disabled
     if counter == 0:
        button_back = Button(root, text="<<" , state = DISABLED)
        button_back.grid(row =1 , column = 0)

     my_label.grid_forget()

     my_label = Label(image = imageList[counter-1])
     my_label.grid(row =0, column =0 , columnspan = 3)

     button_forward = Button(root, text=">>", command =forward)
     button_forward.grid(row =1 , column = 2)
      # update status bar
     status.grid_forget()
     status = Label(root, text="image " +str(counter +1)+" of " +str(len(imageList)),bd = 1, relief = SUNKEN, anchor = E)
     status.grid(row=2, column = 0 , columnspan =3, sticky = W+E, pady = 10)



# triggers when the forward button is pressed
def forward():
     global my_label,counter,button_forward,status
     counter = counter + 1


     button_forward = Button(root, text=">>" , command = forward)
     button_forward.grid(row =1 , column = 2)

     # if the end of the array is reached is reached , the forward button is disabled
     if counter == len(imageList)-1 :
         button_forward = Button(root, text=">>" , state = DISABLED)
         button_forward.grid(row =1 , column = 2)

     my_label.grid_forget()
     # image
     my_label = Label(image = imageList[counter])
     my_label.grid(row = 0 , column = 0, columnspan =3)
     # backButton
     button_back = Button(root, text="<<" , command =back)
     button_back.grid(row =1 , column = 0)
     # update status bar
     status.grid_forget()
     status = Label(root, text="image " +str(counter +1)+" of " +str(len(imageList)),bd = 1, relief = SUNKEN, anchor = E)
     status.grid(row=2, column = 0 , columnspan =3, sticky = W+E, pady = 10)


# putting image on the screen
my_label = Label(image=my_img1)
my_label.grid(row = 0 , column = 0, columnspan =3)


# putting the button on the screen
button_back=Button(root, text ="<<" ,state = DISABLED)
button_exit=Button(root, text ="Exit", command= root.quit)
button_forward=Button(root, text =">>", command = forward)

status =Label(root, text = "image 1 0f " + str(len(imageList)),bd = 1, relief = SUNKEN, anchor = E)
status.grid(row =2 , column = 0 , columnspan =3, sticky = W+E, pady = 10)

button_back.grid(row =1, column =0)
button_exit.grid(row =1, column =1)
button_forward.grid(row =1, column =2)



root.mainloop()
