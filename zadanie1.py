from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_odd_numbers():
    # Нечетные числа в диапазоне 1 < n ≤ 4
    odd_numbers = [n for n in range(2, 5) if n % 2 != 0]
    
    # HTML-шаблон
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Нечетные числа</title>
    </head>
    <body>
        <h1>Нечетные числа в диапазоне 1 &lt; n ≤ 4</h1>
        <p>{{ odd_numbers }}</p>
    </body>
    </html>
    """
    
    return render_template_string(html_template, odd_numbers=", ".join(map(str, odd_numbers)))

if __name__ == "__main__":
    app.run(debug=True)