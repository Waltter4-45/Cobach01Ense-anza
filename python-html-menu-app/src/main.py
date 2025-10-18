from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

from archive import get_archive_list, get_archive_item
from quiz import get_quiz_questions, get_quiz_results

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/archive')
def archive():
    items = get_archive_list()  # Usa la función correcta para la lista
    return render_template('archive.html', items=items)

@app.route('/archive/<item_id>')
def archive_detail(item_id):
    item = get_archive_item(item_id)
    return render_template('archive_detail.html', item=item)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Recupera las preguntas en el mismo orden de la sesión
        questions = session.get('quiz_questions')
        results = get_quiz_results(request.form, questions)
        return render_template('quiz.html', questions=questions, results=results)
    else:
        questions = get_quiz_questions()
        session['quiz_questions'] = questions  # Guarda el orden en la sesión
        return render_template('quiz.html', questions=questions, results=None)

if __name__ == '__main__':
    app.run(debug=True)