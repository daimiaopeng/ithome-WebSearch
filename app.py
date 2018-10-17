from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from sqlite import *
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')
@app.route('/comment',methods=['POST'])
def api():
    if request.method == 'POST':
        text = request.form['text']
        infor = get_infor(text)
        infor = sort_date(infor)
        for i in infor:
            try:
                i[0] = get_image(i[0])
            except:
                i[0] = 'https://quan.ithome.com/statics/images/noavatar.png'
    return render_template('index.html',infor = infor,len_comment=len(infor))


if __name__ == '__main__':
    app.run(port=5003,host='0.0.0.0')
