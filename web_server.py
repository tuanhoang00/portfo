from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html', name=username)
#
#
# @app.route('/<username>/<int:post_id>')
# def hello_world2(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route('/')
def my_home():
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/<string:page_name>')
def my_route(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong try again'





