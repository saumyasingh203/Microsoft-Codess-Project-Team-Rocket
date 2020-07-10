from flask import Flask, request, render_template,jsonify
A = ( [2, 5, 7],
      [4, 7, 9],
      [7, 8, ""] )

app = Flask(__name__)

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/background_process')
def background_process():
    return jsonify(A)

if __name__ == '__main__':
    app.run(debug=True)

