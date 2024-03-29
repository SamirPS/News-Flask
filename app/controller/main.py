from flask import Flask,Blueprint, session, redirect, url_for, request,render_template
from newsscrapper import fr
from newsscrapper import en
from newsscrapper import es

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
  return render_template("index.html")

@bp.route('/fr')
def newsfr():
    return render_template("fr.html",L=[["LeMonde",fr.MondeSC()],["LeParisien",fr.ParisSC()],["MediaPart",fr.MediaPartSC()],["BFMTV",fr.BmftvSC()],["Liberation",fr.LibeSC()],["FranceTvINFO",fr.FTISC()]])

@bp.route('/en')
def newsen():
    return render_template("en.html",L=[["CNN",en.CNNSC()],["FoxNews",en.FoxNewsSC()],["AbcNews",en.ABCNewsSC()],["TheGuardian",en.TheGuardianSC()],["TheNewYorkTimes",en.TheNewYorkTimesSC()]])

@bp.route('/es')
def newses():
    return render_template("es.html",L=[["EFE",es.EFESC()],["ELPAIS",es.ELPAISSC()]])