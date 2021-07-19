from flask import Flask, render_template, request

app = Flask(__name__)


def int_to_Roman(number):
    num = int(number)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


@app.route('/')
def index():
    return render_template("index.html", developer_name= "C8164-Adam")


@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        number = request.form.get("number")
        number_roman = int_to_Roman(number)
        return render_template("result.html", number_roman = number_roman, developer_name = "C8164-Adam", number_decimal = number)
    else:
        return render_template("result.html", developer_name="C8164-Adam")

if __name__=="__main__":
    # app.run(debug=True),
    app.run(host='0.0.0.0', port=80)
