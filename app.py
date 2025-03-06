from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def main():
    print("H")
    return render_template("index.html")

@app.route("/fetch_item", methods=["POST"])
def fetch_item():
    return render_template("recipe_nutrient.html")

@app.route("/fetch_recipe_item", methods=["POST"])
def fetch_recipe_item():
    url = "https://low-carb-recipes.p.rapidapi.com/search"

    querystring = {}
    headers = {
        "x-rapidapi-key": "584798a762mshf8791655801aa07p193ab2jsnc75276e6aecf",
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }

    itemname = request.form.get("item")
    querystring ["name"] = itemname
    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    print(data[0].keys())

    return render_template("display_item.html", data=data)

@app.route("/fetch_ct", methods=["POST"])
def fetch_ct():
    return render_template("recipe_cookTime.html")

@app.route("/fetch_recipe_ct", methods=["POST"])
def fetch_recipe_ct():
    url = "https://low-carb-recipes.p.rapidapi.com/search"

    querystring = {}
    headers = {
        "x-rapidapi-key": "584798a762mshf8791655801aa07p193ab2jsnc75276e6aecf",
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }

    ct = request.form.get("ct")
    querystring ["maxCookTime"] = ct
    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    print(data[0].keys())

    return render_template("display_item.html", data=data)

@app.route("/fetch_recipe_random", methods=["POST"])
def fetch_recipe_random():
    url = "https://low-carb-recipes.p.rapidapi.com/random"

    headers = {
        "x-rapidapi-key": "584798a762mshf8791655801aa07p193ab2jsnc75276e6aecf",
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data=response.json()

    return render_template("display_item1.html", data=data)

@app.route("/fetch_id", methods=["POST"])
def fetch_id():
    return render_template("recipe_id.html")
@app.route("/fetch_recipe_id", methods=["POST"])
def fetch_recipe_id():
    url = "https://low-carb-recipes.p.rapidapi.com/recipes/"

    headers = {
        "x-rapidapi-key": "584798a762mshf8791655801aa07p193ab2jsnc75276e6aecf",
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }

    id = request.form.get("id")
    url=url+id
    response = requests.get(url, headers=headers)
    data=response.json()
    print(data)

    return render_template("display_item1.html", data=data)

if __name__=='__main__':
    app.run(debug=True, port=5001)