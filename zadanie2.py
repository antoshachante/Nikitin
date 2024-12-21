from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_movies():
    # Многомерный массив
    movies_by_genre = {
        "Комедия": ["Операция «Ы» и другие приключения Шурика", "Иван Васильевич меняет профессию", "Назад в будущее"],
        "Мелодрама": ["Унесённые ветром", "Великий Гэтсби", "Амели"],
        "Детектив": ["Убийство в «Восточном экспрессе»", "Молчание ягнят", "Китайский квартал"],
        "Фантастика": ["Терминатор", "Начало", "Марсианин"]
    }
    
    # HTML-шаблон для отображения данных
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Фильмы по жанрам</title>
    </head>
    <body>
        <h1>Фильмы, организованные по жанрам</h1>
        <ul>
        {% for genre, movies in movies_by_genre.items() %}
            <li><strong>{{ genre }}:</strong>
                <ul>
                {% for movie in movies %}
                    <li>{{ movie }}</li>
                {% endfor %}
                </ul>
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """
    
    return render_template_string(html_template, movies_by_genre=movies_by_genre)

if __name__ == "__main__":
    app.run(debug=True)
