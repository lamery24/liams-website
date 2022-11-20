from flask import Flask, render_template, jsonify

app=Flask(__name__)

DL=[
  {
    'id':1,
    'title':'Doha',
    'country': 'QAT',
    'date':'13 May 2022',
   'site':'https://doha.diamondleague.com/programme-results-doha/'
  },
    {
    'id':2,
    'title':'Birmingham',
    'country': 'GBR',
    'date':'21 May 2022',
      'site':'https://doha.diamondleague.com/programme-results-london/'
  },
      {
    'id':3,
    'title':'Eugene',
    'country': 'USA',
    'date':'28 May 2022',
        'site':'https://doha.diamondleague.com/programme-results-eugene/'
  },
]

@app.route("/")
def hp():
  return render_template('index.html',
                        dl=DL)



@app.route("/api/dlsched")
def dl_sched():
  return jsonify(DL)

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500

  
@app.route("/elite-results/")
def er():
  return render_template('elite-results.html')

@app.route("/archive/")
def col_archive():
  return render_template('carchive.html')


@app.route("/media/")
def media():
  return render_template('media.html')

#ARTICLES
@app.route("/articles/xc_champs_recap_22/")
def ar_xc_22():
  return render_template('articles/xc_champs_recap_22.html')

@app.route("/articles/xc_champs_2022/")
def ar_xc_22():
  return render_template('articles/xc_champs_2022.html')



  
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)