from flask import Flask
import seaborn as sns

app = Flask(__name__)

tips = sns.load_dataset('tips')

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/table')
def table_view():
    html = '<div>' + \
           '<h1>Table of tips data</h1>' + \
           '<p>This table contains data from the seaborn tips dataset</p>' + \
           tips.head(20).to_html(table_id='tips', border=6, index=False, justify='center') + \
           '</div>'
    return html

if __name__ == '__main__':
    app.run(debug=True) 