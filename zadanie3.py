import random
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def random_numbers():
    numbers = []
    n = 0
    
    if request.method == 'POST':
        try:
            # Получаем количество чисел из формы
            n = int(request.form['count'])
            if n > 0:
                # Генерируем массив из n случайных чисел
                numbers = [random.randint(1, 100) for _ in range(n)]
        except ValueError:
            numbers = ["Ошибка: Введите правильное число!"]

    # HTML-шаблон
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Генератор случайных чисел</title>
    </head>
    <body>
        <h1>Генератор массива случайных чисел</h1>
        <form method="post">
            <label for="count">Введите количество чисел:</label>
            <input type="number" id="count" name="count" min="1" required>
            <button type="submit">Сгенерировать</button>
        </form>
        {% if numbers %}
            <h2>Результат:</h2>
            <p>{{ numbers }}</p>
        {% endif %}
    </body>
    </html>
    """
    
    return render_template_string(html_template, numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)
