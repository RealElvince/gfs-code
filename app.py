from flask import Flask, render_template, request
import json
from generators.gfs_generator import code_generator

app = Flask(__name__)

# Load counties and constituencies data
with open("data/kenya_counties.json") as f:
    kenya_counties = json.load(f)

@app.route('/')
def index():
    
    return kenya_counties

if __name__ == "__main__":
    app.run(debug=True)

