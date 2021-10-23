import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request


def output():
   
        # urls = request.form["url"]
        urls=input("Enter the url:-")
        print(urls)
        grab = requests.get(urls)
        soup = BeautifulSoup(grab.text, 'html.parser')
        
        # # opening a file in write mode
        f = open("test1.csv", "w+")
        # traverse paragraphs from soup
        for link in soup.find_all("a"):
            data = link.get('href')
            f.write(data)
            f.write("\n")
        
        f.close()
output()