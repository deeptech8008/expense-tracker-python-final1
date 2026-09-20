from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Load data
def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open("expenses.json", "w") as f:
        json.dump(data, f, indent=4)

# Home page (form)
@app.route("/")
def home():
    return render_template("index.html")

# Add expense
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    amount = float(request.form["amount"])

    data = load_data()
    data.append({"name": name, "amount": amount})
    save_data(data)

    return redirect("/view")

# View expenses
@app.route("/view")
def view():
    data = load_data()
    total = sum(item["amount"] for item in data)
    return render_template("view.html", expenses=data, total=total)

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)