from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Fronted Developer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backened Engineer',
    'location': 'Sna Francisco, USA',
    'salary': '$ 120,000'
  },
]


@app.route("/")
def hello_enantiomer():
  return render_template('home.html', 
                         jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

  
#localjost chhaiye
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
