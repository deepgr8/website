import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request

app = Flask(__name__)

def ho():
    return render_template('/templates/index.html')

@app.route('/',methods=['POST','GET'])
def output():
    
    if request.method == 'POST':
      
        urls = request.form["url"]
        
        grab = requests.get(urls)
        soup = BeautifulSoup(grab.text, 'html.parser')
        
        # # opening a file in write mode
        f = open("urlfile.csv", "w+")
        # traverse paragraphs from soup
        for link in soup.find_all("a"):
            data = link.get('href')
            f.write(data)
            f.write("\n")
        
        f.close()
        return render_template('/templates/downl.html')
@app.route('/download')    
def download_file():
    path="urlfile.csv"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
