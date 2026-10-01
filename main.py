from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

goal = {
    "name": "",
    "target": 0
}


@app.route("/")
def home():
    total = sum(expense["amount"] for expense in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        goal=goal
    )


@app.route("/add", methods=["POST"])
def add_expense():
    expense = request.form["expense"]
    amount = int(request.form["amount"])
    category = request.form["category"]
    date = request.form["date"]

    expenses.append({
        "expense": expense,
        "amount": amount,
        "category": category,
        "date": date
    })

    return redirect("/")


@app.route("/set-goal", methods=["POST"])
def set_goal():
    goal["name"] = request.form["goal_name"]
    goal["target"] = int(request.form["goal_target"])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)