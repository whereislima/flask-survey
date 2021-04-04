from flask import Flask, request, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "figs"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def homepage():

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)

@app.route('/question/<int:question_id>')
def question(question_id):
    
    question = satisfaction_survey.questions[question_id]
 
    return render_template('question.html', question=question)

@app.route('/answer')
def answer():

    answer = request.form["answer"]

    responses.append(answer)

    # redirect next question

@app.route('/completed')
def completed():

  return render_template('completed.html')