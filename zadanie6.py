from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_numbers():
    # Создание массива с целыми и вещественными числами
    numbers = [42, 3.14, 100, 2.718, 7, 5.0, 35, 8.9]
    
    # Форматирование строк с шириной 20 символов
    formatted_numbers = [f"{num:20}" for num in numbers]

    # HTML-шаблон для вывода на веб-страницу
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Массив чисел</title>
    </head>
    <body>
        <h1>Массив целых и вещественных чисел</h1>
        <pre>
        {% for num in formatted_numbers %}
            {{ num }}
        {% endfor %}
        </pre>
    </body>
    </html>
    """
    
    # Отправка отформатированных данных в шаблон
    return render_template_string(html_template, formatted_numbers=formatted_numbers)

if __name__ == "__main__":
    app.run(debug=True)
