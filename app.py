# Created By: 
#     Grettel Canepari
#     Katherine Lee
#     Mandar Gogate
#     Petra Alex
#     Preet Puri
#     Sweta Shekhar
# Created On: 01/01/2020
# Updated On: 01/10/2020

#https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask
#https://stackoverflow.com/questions/10572498/importerror-no-module-named-sqlalchemy

from flask import Flask, jsonify, render_template, flash
import dao as db

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    htmlTag ="""<html>
                <table>
                
                    <tr>
                        <td> To get all USA Cities json for Accidents & Population - use </td>
                        <td> /allcities </td>
                    </tr>                   
                    <tr>
                        <td> To get only GA Cities json for Accidents & Population - use </td>
                        <td> /gacities </td>
                    </tr>              
                <table>
                <html>
            """
    return htmlTag

@app.route("/allcities")
def all_city_Population():
    return db.getUSCityPopulation()

@app.route("/gacities")
def ga_city_Population():
    return db.getGACityPopulation()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()