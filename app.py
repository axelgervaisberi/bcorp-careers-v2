from flask import Flask, render_template

app = Flask(__name__)

BOUNTIES = [
  {
    'id': 1,
    'location': 'Cocody, Abidjan CI',
    'objective': 'AI Face Generator with Python',
    'amount': 'XOF 3 000 000'
  },
  {
    'id': 2,
    'location': 'Akandjé, Bingerville CI',
    'objective': 'Voting app with Java Server Faces',
    'amount': 'XOF 1 000 000'
  },
  {
    'id': 3,
    'location': 'Mockeyville, Grand-Bassam CI',
    'objective': 'CRUD app with Excel and Power BI',
    'amount': 'XOF 2 000 000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         bounties=BOUNTIES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
