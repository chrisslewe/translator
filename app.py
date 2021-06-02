#imports
from flask import Flask, render_template, request
from easynmt import EasyNMT

model = EasyNMT('opus-mt')

app = Flask(__name__)
app.static_folder = 'static'





#define app routes
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the translation response
def get_bot_response():
    userInput = request.args.get('msg')
    taal = request.args.get('taal')
    print(taal)
    print(userInput)
    return model.translate(userInput, target_lang='en', source_lang = taal)
if __name__ == "__main__":
    app.run()