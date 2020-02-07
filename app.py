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
                        <td> To get city json - use </td>
                        <td> /city </td>
                    </tr>                   
                
                <table>
                <html>
            """
    return htmlTag

@app.route("/city")
def cityPopulation():
    return db.getCityPopulation()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()