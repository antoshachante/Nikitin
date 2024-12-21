from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None

    if request.method == 'POST':
        try:
            # Получение чисел и операции из формы
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            # Выполнение указанной операции
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Деление на ноль невозможно."
            else:
                error = "Некорректная операция."
        except ValueError:
            error = "Ошибка: Введите корректные числа."

    # HTML-шаблон
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Калькулятор</title>
    </head>
    <body>
        <h1>Веб-калькулятор</h1>
        <form method="post">
            <label for="num1">Первое число:</label>
            <input type="number" step="any" id="num1" name="num1" required>
            <br><br>
            <label for="num2">Второе число:</label>
            <input type="number" step="any" id="num2" name="num2" required>
            <br><br>
            <label for="operation">Операция:</label>
            <select id="operation" name="operation" required>
                <option value="add">Сложение</option>
                <option value="subtract">Вычитание</option>
                <option value="multiply">Умножение</option>
                <option value="divide">Деление</option>
            </select>
            <br><br>
            <button type="submit">Вычислить</button>
        </form>
        {% if result is not none %}
            <h2>Результат: {{ result }}</h2>
        {% elif error %}
            <h2 style="color: red;">Ошибка: {{ error }}</h2>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html_template, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
