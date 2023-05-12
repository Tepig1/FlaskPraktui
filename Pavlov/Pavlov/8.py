from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index1.html', name='Nikita')
@app.route('/adout')
def adout():
    print(url_for('adout'))
    return render_template('index.html')

with  app.test_request_context ():
    print(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)