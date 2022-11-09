from flask import Flask, render_template, jsonify

app=Flask(__name__)

DL=[
  {
    'id':1,
    'title':'Doha',
    'country': 'QAT',
    'date':'13 May 2022'
  },
    {
    'id':2,
    'title':'Birmingham',
    'country': 'GBR',
    'date':'21 May 2022'
  },
      {
    'id':3,
    'title':'Eugene',
    'country': 'USA',
    'date':'28 May 2022'
  },
]

@app.route("/")
def hp():
  return render_template('home.html',
                        dl=DL)

@app.route("/api/dlsched")
def dl_sched():
  return jsonify(DL)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)