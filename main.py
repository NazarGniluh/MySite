from flask import Flask, render_template



app = Flask("Spoli")
database = [
    (0, "<3 T-SHIRT", "Футболка - <3 T-SHIRT вироблена для людей яких люблять ", 2000, "Футболка", "coftoshka.png"),
    (1, "Олімпійка", "Олімпійка -  вироблена для класного стилю і кайфа ", 6300, "Олімпійка", "opinnnn.jpg"),
    (2, "Шапка і шарф", "Шапка і Шарф - це комбо для теплоти і стилю ", 799, "Шапка і шарф", "sharf.jpg"),
    (3, "Чорна Шапка Bad Potsa", "Bad Potsa - це стильна шапочка для +вайба ", 1999, "Шапка Bad Potsa", "chjrnisapka.jpg"),
    (4, "Зелена Шапка Bad Potsa", "Bad Potsa - ці шапки унікальні та красиві бажаю кожному купити ", 1699, " Зелена Шапка Bad Potsa", "shaaapkaa.jpg"),
    (5, "Штани", "Штани для дівчат - вироблені для комфорта і модності  ", 1599, "Штани для дівчат", "stanushi.jpeg"),
    (6, "Штани", "Штани для хлопців - штани s клас ну топ просто  ", 1399, "Штани для хлопців", "pasuku1.jpg"),
    (7, "Рукавички", "Рукавички для дівчат - для файних ручків та теплоти  ", 499, "Рукавички для дівчат", "rukavi.jpg"),
    (8, "Худі", "Худі від Balenciaga  - це круто і стильно   ", 2999, "Худі від Bakenciaga", "balenci.jpg"),
    (9, "Zip", "Зіпка від Balenciaga  - Модняк 100% Париж на спині ну БОМБА   ", 5699, "Зіпка від Bakenciaga", "hudakk.jpg"),
    (10, "Zip Rick Owens", "Зіпка від Rick Owens  - Виготовлена з преміальних матеріалів,вона має лаконічний дизайн модний  ", 5299, "Зіпка від Rick Owens", "rickowenss.jpg")
]




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html", products=database)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if "Slopi" == "__main__":
    app.run(debug=True)


app.run()