from flask import Flask, render_template, request, redirect
import utils
import query

app = Flask("__name__")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        animal_id = request.form["animal_id"]
        return redirect(f"/{animal_id}")


@app.route("/<int:animal_id>")
def animalid(animal_id):
    animals = query.connect("SELECT rowid, name, breed, color1, age_upon_outcome  FROM animals")
    _, name, breed, color1, date_of_birth = utils.animal_for_id(animals, animal_id)

    return render_template("search_for_id.html", name=name, breed=breed, color=color1, birth=date_of_birth)


if __name__ == "__main__":
    app.run(debug=True)
