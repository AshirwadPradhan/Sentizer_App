from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class sent_tb():
    '''
    sentiment analysis using textblob
    '''
    def __init__(self):
        pass
    
    def saySentiment(self, text):
        '''
        predict the sentiment based on TextBlob
        tweaks made:
        TextBlob seems to make predictions mostly around 0 so to avoid getting biased
        we used a threshold as 0.0001.
        This performed better than other values
        '''
        
        analysis = TextBlob(text)
        if analysis.sentiment.polarity <= -0.0001:
            if analysis.sentiment.polarity <= 0:
                _overallSent = 'Negative: '+str(analysis.sentiment.polarity)
        elif analysis.sentiment.polarity >= 0.0001:
            if analysis.sentiment.polarity > 0:
                _overallSent = 'Positive: '+str(analysis.sentiment.polarity)
        else:
            _overallSent = 'Neutral'

        return _overallSent
    

class sent_vs():
    '''
    sentiment analysis using VaderSentiment
    '''
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
    
    def saySentiment(self, text):

        analysis = self.analyzer.polarity_scores(text)
        # print(analysis)
        try :
            if not analysis['pos'] > 0.1:
                if analysis['pos'] - analysis['neg'] < 0:
                    _overallSent = 'Negative: -'+str(analysis['neg'])
            elif not analysis['neg'] > 0.1:
                if analysis['pos'] - analysis['neg'] > 0:
                    _overallSent = 'Positive: '+str(analysis['pos'])
            else:
                _overallSent = 'Neutral'
            
            if analysis['neu'] == 1:
                _overallSent = 'Neutral'
            
            return _overallSent
            
        except Exception:
            return 'None'

if __name__ == '__main__':
    # text = 'I am a very bad person and I will kill you'
    # text = 'Woah what a tutorial'
    text = 'You are a bad person, are not you ?'
    o_tb = sent_tb()
    print(o_tb.saySentiment(text))
    o_vs = sent_vs()
    print(o_vs.saySentiment(text))