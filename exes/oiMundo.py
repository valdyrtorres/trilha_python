# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:44:43 2019

@author: Valdir
"""

from flask import Flask

# __name__ é a variável que representa o nome do módulo corrente
app = Flask(__name__)

@app.route("/")

def oiMundo():
    return "Oi Mundo!"

if(__name__ == "__main__"):
    app.run()
