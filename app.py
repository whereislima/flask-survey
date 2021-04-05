from flask import Flask, request, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "figs"

debug = DebugToolbarExtension(app)

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False

responses = []

@app.route('/')
def homepage():
    """ renders home page """
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)

@app.route('/begin')
def begin_survey():
    """ redirects to first question """
    return redirect('/question/0')


@app.route('/question/<int:question_id>')
def question(question_id):

    if (responses is None):
        return redirect('/')

    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect('/completed')
    
    if(len(responses) != question_id):

        flash(f"You are on the wrong question {question_id}")
        return redirect(f"/question/{len(responses)}")

    
    question = satisfaction_survey.questions[question_id]
 
    return render_template('question.html', question=question)

@app.route('/answer', methods=["POST"])
def answer():

    answer = request.form["answer"]

    responses.append(answer)

    print("PRINT PRINT PRINT PRINT PRINT responses", responses)

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect('/completed')
    else:
        return redirect(f"question/{len(responses)}")

@app.route('/completed')
def completed():

  return render_template('completed.html')


