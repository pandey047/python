from win32com.client import Dispatch
import requests
import json
def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak(" Good After noon  news for today Lets Begin ")
    url='https://newsapi.org/v2/top-headlines?country=in&apiKey=e8ac8edbcc854113b2a8d68f1b6e1503'

    news=requests.get(url).text
    news_json=json.loads(news)
    
    arts=news_json['articles']
    for articles in arts:
        print(articles['title'])
        speak(articles['title'])
        speak('Next news ...Pay attention')
    speak('Thanks for being with us')

