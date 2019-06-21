import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
import urllib.request
import urllib.error
import json


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'FizzBot'
        self.domain = 'https://api.noopschallenge.com'
        self.question_url= '/fizzbot'
        self.message = ''
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.questionLabel = QLabel(self)
        self.questionLabel.setGeometry(50, 50, 500, 150)
        self.answerInput = QTextEdit(self)
        self.answerInput.setGeometry(50, 200, 500, 50)
        self.nextButton = QPushButton('Next', self)
        self.nextButton.setGeometry(300, 250, 100, 30)
        self.nextButton.clicked.connect(self.do_question)
        self.submitButton = QPushButton('Submit', self)
        self.submitButton.setGeometry(200, 250, 100, 30) 
        self.resize(600, 300)
        self.show()
        self.do_question()
    
    def do_question(self):
        print(self.question_url)
        request = urllib.request.urlopen( ('%s%s' % (self.domain, self.question_url)))
        response = request.read().decode('utf-8')
        print(response)
        response_json = json.loads(response)
        self.message = response_json.get('message')
        question_url = response_json.get('nextQuestion')
        if question_url:
            self.question_url = question_url
            self.nextButton.setEnabled(True)
            self.submitButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(False)
            self.submitButton.setEnabled(True)
            
        self.questionLabel.setText(self.message)
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

