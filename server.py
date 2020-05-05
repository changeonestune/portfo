from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/<name>')
def index(name):
	return render_template(name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=="POST":
		data = request.form.to_dict()
		wirte_to_csv(data)
		return render_template("thankyou.html", data = data)
		# return redirect("/thankyou.html")
	else:
		return "something went wrong! Try again"

def wirte_to_file(data):
	with open ("database.txt", "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"{email}, {subject}, {message}\n")

def wirte_to_csv(data):
	with open ("database.csv", mode = "a", newline = "") as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])