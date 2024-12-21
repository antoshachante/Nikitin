from flask import Flask, render_template_string

app = Flask(__name__)

# Имя файла для хранения числа
FILE_NAME = "counter.txt"

def get_and_increment_counter():
    try:
        # Читаем текущее значение из файла
        with open(FILE_NAME, "r") as file:
            counter = int(file.read().strip())
    except FileNotFoundError:
        # Если файл не найден, создаем его с начальным значением
        counter = 0

    # Увеличиваем значение на 1
    counter += 1

    # Сохраняем обновленное значение в файл
    with open(FILE_NAME, "w") as file:
        file.write(str(counter))

    return counter

@app.route('/')
def display_counter():
    counter = get_and_increment_counter()

    # HTML-шаблон
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Счётчик запусков</title>
    </head>
    <body>
        <h1>Счётчик запусков программы</h1>
        <p>Текущее значение счётчика: <strong>{{ counter }}</strong></p>
    </body>
    </html>
    """
    return render_template_string(html_template, counter=counter)

if __name__ == "__main__":
    app.run(debug=True)
