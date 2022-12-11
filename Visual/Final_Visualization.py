import pandas as pd
import numpy as np

import cufflinks as cf
import plotly.graph_objects as go
import chart_studio.plotly as py

cf.go_offline(connected = True)

from IPython.core.display import display, HTML
import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

###################################################################################

from flask import  Flask, request, make_response, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')


@app.route('/') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_first(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('index.html')


@app.route('/base') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_base(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('index.html')


@app.route('/404.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_404(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('404.html')

    
@app.route('/401.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_401(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('401.html')


@app.route('/charts.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_charts(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('charts.html')


@app.route('/layout-sidenav-light.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_layout_sidenav_light(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('layout-sidenav-light.html')


@app.route('/layout-static.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_layout_static(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('layout-static.html')

    
@app.route('/login.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_login(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('login.html')


@app.route('/password.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_password(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('password.html')


@app.route('/register.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def register(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('register.html')

@app.route('/tables.html') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_tables(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('tables.html')



if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = '8080')