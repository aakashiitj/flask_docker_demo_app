# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:42:54 2021

@author: aakasharora
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "welcome to the default webpage. Created as a part of cloud computing assignment"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
