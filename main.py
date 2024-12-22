from flask import Flask, render_template



app = Flask("Spoli")
database = [
    (0, "<3 T-SHIRT", "Футболка - <3 T-SHIRT вироблена для людей яких люблять ", 2000, "Футболка", "coftoshka.png"),
    (1, "FLISKA JACKET", "Куртка - FLISKA JACKET вироблена для теплості людей і душі і +вайбик ", 6300, "Куртка", "opinnnn.jpg")
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