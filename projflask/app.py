from flask import Flask, render_template, url_for
app = Flask(__name__, static_folder='static')


# Define a route for the static files
@app.route('/static/<path:path>')
def static_files(path):
    return app.send_static_file(path)

# Define your other routes
@app.route('/')
def home():
    return render_template('front.html')

@app.route('/signpage')
def signpage():
    return render_template('signpage.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/moni1')
def moni1():
    return render_template('moni1.html')

@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/logmoni1')
def logmoni1():
    return render_template('logmoni1.html')

@app.route('/logmoni2')
def logmoni2():
    return render_template('logmoni2.html')

@app.route('/monitering')
def monitering():
    return render_template('monitering.html')

@app.route('/forget')
def forget():
    return render_template('forget.html')


@app.route('/aboutus2')
def aboutus2():
    return render_template('aboutus2.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/contactus2')
def contactus2():
    return render_template('contactus2.html')

if __name__ == '__main__':
    app.run(debug=True)
