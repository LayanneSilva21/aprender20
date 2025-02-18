from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de perguntas (exemplo)
questions = [
    {
        'question': 'Qual é a capital do Brasil?',
        'answers': ['Brasília', 'Rio de Janeiro', 'São Paulo'],
        'correct': 0
    },
    # ... outras perguntas
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for index, question in enumerate(questions):
        user_answer = request.form.get(f"question_{index+1}")
        if user_answer is not None and int(user_answer) == question['correct']:
            score += 1
    return render_template('result.html', score=score)

@app.template_filter()
def enumerate_items(items):
    return enumerate(items)

app.jinja_env.filters['enumerate_items'] = enumerate_items

if __name__ == '__main__':
    app.run(debug=True)
