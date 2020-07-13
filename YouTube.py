from tkinter import *
from pytube import YouTube

#inisialisasi tkinter
x = Tk()
#setting Judul GUI
x.title("Aplikasi Pengunduh Video YouTube")

def unduh():
    try:
        var.set("Sedang Mengunduh")
        x.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video telah terunduh")
    except Exception as e :
        var.set("Link Salah")
        x.update()
        link.set("Masukan link yang tepat")

Label(x, text = "Aplikasi Pengunduh Video Youtube", font = "Consolas 15 bold").pack()
#deklarasi StringVar
var = StringVar()

#setting text
var.set("Masukan Link")
#membuat Entry
Entry(x, textvariable = var, width = 40).pack(pady=10)

#Setting Link
link =StringVar()
Entry(x, textvariable = link, width = 40).pack(pady=10)

#memanggil fungsi unduhan
Button(x, text="Unduh Video", command=unduh).pack()
x.mainloop()
