from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=["GET", 'POST'])
def result():
    if request.method =="POST":
        f_n = request.form.get('foydalanuvchi_nomi')
        t = request.form.get('telefon')
        y = request.form.get('yosh')
        y = int(y)

        if len(f_n) > 4 and "+" in t and len(t) >= 11 and y >= 18 and y <= 99:
            res = [f_n, t, y]
        else:
            res = ['Malumotlar notogri kiritldi']

        return render_template('res.html', res = res)

    return render_template('index.html')    




if __name__ == '__main__':
    app.run(debug=True)

