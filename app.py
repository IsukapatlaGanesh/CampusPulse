from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    title = request.form['title']
    description = request.form['description']

    print("Issue Title:", title)
    print("Description:", description)

    return f"""
    <h1>Issue Submitted Successfully</h1>
    <p><strong>Title:</strong> {title}</p>
    <p><strong>Description:</strong> {description}</p>
    """


if __name__ == '__main__':
    app.run(debug=True)