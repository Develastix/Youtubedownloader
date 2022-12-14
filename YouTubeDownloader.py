from importlib.metadata import EntryPoint
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

import os #cw

#faster readable code in function
def cwWidgets():
    
    #youtube link label
    link_label = Label(root, text = "  Youtube URL:  ", bg = "#EAF0EE", font =("Verdana 10 bold", 10))
    link_label.grid(row=1, column=0, padx=5, pady=5)
      
    #youtube link text entry point
    root.link_text = Entry(root, width=60, textvariable=video_link, font =("Verdana 10 bold", 10))
    root.link_text.grid(row=1, column=1, padx=5, pady=5)
    
    #destination label
    link_label = Label(root, text = " Download path: ", bg = "#EAF0EE", font =("Verdana 10 bold", 10))
    link_label.grid(row=2, column=0, padx=5, pady=5)
    
    #destination label text entry point
    root.dest_text = Entry(root, width=60, textvariable=download_path, font =("Verdana 10 bold", 10))
    root.dest_text.grid(row=2, column=1, padx=5, pady=5)
    
    #buttons
    browse_button = Button(root, text="Browse", command=browse, width=10, bg = "#EAF0EE")
    browse_button.grid(row=2, column=2, padx=1, pady=1)
    
    download_button = Button(root, text="Download Video", command=download_video, width=25, bg = "#EAF0EE")
    download_button.grid(row=3, column=1, padx=1, pady=1)
    
    #select quality
    # quality_high = Radiobutton(root, text="mp4 High Quality", variable=IntVar(), value=1, command=sel)
    # quality_high.grid(row=4, column=2, padx=1, pady=1)
    
    # quality_low = Radiobutton(root, text="Low Quality", variable=IntVar(), value=1, command=sel)
    # quality_low.grid(row=3, column=2, padx=1, pady=1)
    
    # def sel():
    #     selection = "You selected the option " + str(var.get())
    #     label.config(text = selection)    
    
    label = Label(root)

#function to set destination folder    
def browse():
    download_dir = filedialog.askdirectory(initialdir="Your directory path")    
    download_path.set(download_dir)  

#function for download button
def download_video():
    url = video_link.get()
    folder = download_path.get()
    
    #the url has vaious streams so must specify to get the first one
    get_video = YouTube(url) 
    
    
    # get_stream = get_video.streams.first().download(filename='filename')
    # get_stream = get_video.streams.filter(subtype='mp4').first().download(filename='filename') 
    get_stream = get_video.streams.get_highest_resolution()
     
    get_stream.download(folder)
    
    messagebox.showinfo("Success", "Download successful to: \n"+ folder)
      
#tkinter copy paste cut functions for cyrillic     
#Cut text  
def cut_text(e): # is is kust a holding variable
    global selected
    #check to see if we use keyboard shortcuts or menu
    if e:
        selected = root.clipboard_get()
    else:    
        if my_text.selection_get():
            #grab selected text from text box
            selected = my_text.selection_get()
            #delete selected text 
            my_text.delete("sel.first", "sel.last") #check code for these 3 functions
            #clear the clipboard then append
            root.clipboard_clear() #clear first in case menu was used to copy
            root.clipboard_append(selected) #add the selected text to the clipboard            

#Copy text  
def copy_text(e): # is is kust a holding variable
    global selected
    #check to see if we use keyboard shortcuts or menu
    if e:
        selected = root.clipboard_get() # get from the windows clipboard    
    if my_text.selection_get():
        #grab selected text from text box
        selected = my_text.selection_get()
        #clear the clipboard then append
        root.clipboard_clear() #clear first in case menu was used to copy
        root.clipboard_append(selected) #add the selected text to the clipboard
                
#Paste text  
def paste_text(e): # is is kust a holding variable
    global selected
    #checxk to see if keyboard shortcut used
    if e:   
        selected = root.clipboard_get()    
    else:
        if selected:
            position = my_text.index(INSERT)
            mytext.insert(position, selected)       
        

#create instance of tkinter
root = tk.Tk()

#window parameters
root.geometry("760x220")
root.resizable(False, False)
root.title("CW YouTube Downloader")
root.config(background="#000000")

video_link = StringVar()
download_path = StringVar()

#add bindings for cyrilic keyboard copy and paste
#see functions
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

cwWidgets()

root.mainloop()

