from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html', company_name="Band-Name")

@app.route("/", methods=["POST", "GET"])
def generate():
  band_name = request.form["city_name"] + request.form["pet_name"]
  return render_template('home.html', name=band_name)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
