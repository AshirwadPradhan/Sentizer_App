from flask import Flask, render_template, request, make_response
from driver import sent_tb, sent_vs


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_data()
    text = str(text)
    print(text)
    o_tb = sent_tb()
    t_tb = o_tb.saySentiment(text)
    t_tb = "TextBlob predicts: "+t_tb
    o_vs = sent_vs()
    t_vs = o_vs.saySentiment(text)
    t_vs = " and VaderSentiment predicts: "+t_vs
    predicted_text = t_tb + t_vs
    print(predicted_text)
    return make_response(str(predicted_text), 200)


if __name__ == '__main__':
    app.run()