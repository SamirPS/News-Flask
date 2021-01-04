from flask import Flask,render_template
from newsscrapper import fr
from newsscrapper import en


app= Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/fr')
def newsfr():
    return render_template("fr.html",LeMonde =fr.MondeSC(),
    LeParisien=fr.ParisSC(),
    MediaPart=fr.MediaPartSC(),
    BFMTV =fr.BmftvSC(),
    Liberation =fr.LibeSC(),
    FranceTvINFO =fr.FTISC())

@app.route('/en')
def newsen():
    return render_template("en.html",CNN =en.CNNSC(),
    FoxNews=en.FoxNewsSC(),
    AbcNews= en.ABCNewsSC(),
    TheGuardian= en.TheGuardianSC())