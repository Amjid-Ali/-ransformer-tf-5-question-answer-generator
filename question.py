from questiongenerator import QuestionGenerator,print_qa
from questiongenerator import print_qa

from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello World'

@app.route('/data',methods=['GET','POST'])
def info():
        text=request.get_json()
        qg = QuestionGenerator()
        qa_pairs=qg.generate(text["question"], num_questions=text["count"],answer_style='multiple_choice')
        print(print_qa(qa_pairs))
        return jsonify({"answer":qa_pairs})

if __name__ == '__main__':
   app.run()

# text_file="text.txt"
# with open(text_file, 'r') as file:
#         text_file = file.read()

# qg = QuestionGenerator()
# qa_pairs=qg.generate(text_file, num_questions=5,answer_style='multiple_choice')

# print_qa(qa_pairs)

