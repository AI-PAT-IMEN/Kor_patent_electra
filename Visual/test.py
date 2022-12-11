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



display(HTML("<style>.container { width:80% !important; }</style>"))






from flask import  Flask, request, make_response, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_url_path= '/static')


@app.route('/') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_first(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('/templates/index.html')


@app.route('/2') # 라우팅 주소에 있는 변수를 벡엔드에서 받아서 다시 프론트 엔드로 전달할 수 있다.
def get_second(): # routing에 받은 변수를 함수에 사용할 수 있게, ()안에 써준다.
    return render_template('/templates/404.html')

    

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = '8080')