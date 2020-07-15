#import
import  requests
from bs4 import BeautifulSoup

def scrapeinstagram(soup1):
    #Empty List (Menyimpan informasi)
    Data = []

    #Melakukan Looping
    for meta in soup1.find_all (name="meta", attrs={"property" : "og:description"}):
        #Menyimpan di list Data
        Data = meta["content"].split()

    #[Banyaknya followers, Followers, Banyaknya yang diikuti, following, banyaknya postingan, post, ... ]

    pengikut = Data[0]
    diikuti =  Data[2]
    post    = Data[4]

    #menampilkan Hasil
    print("Jumlah Postingan : ", post)
    print("Jumlah Pengikut  : ", pengikut)
    print("Jumlah yang diikuti : ", diikuti)


if __name__ == "__main__":
    #Memintan untuk memasukan username
    user = input("Masukan Username:")

    #url instagram
    url = "https://www.instagram.com/" + user

    #Menyimpan respon
    page = requests.get(url)

    #html.parser
    soup = BeautifulSoup(page.text, "html.parser")

    scrapeinstagram(soup)