from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница с формой
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Обработчик POST-запроса
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')  # Получаем данные из формы
    print(f'Получение данных: {data}')
    return 'ДАнные получены успешно!'

if __name__ == '__main__':
    app.run(debug=True)