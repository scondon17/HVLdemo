from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book_name = request.form['book_name']
        rating = request.form['rating']
        return f'Thank you for submitting {book_name} with a rating of {rating}!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
