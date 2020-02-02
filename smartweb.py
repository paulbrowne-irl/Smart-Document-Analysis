from bottle import Bottle, run, get, static_file
import scripts.graphdb

app = Bottle()

# Python mappings
@app.route('/ReadNeo4j')
def ReadNeo4j():
    db = scripts.graphdb.DB_Access()
    return db.get_greeting("message")

# Default html
@app.route('/<filename>')
def server_static(filename):
    return static_file(filename, root='www')

# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="www/css")

@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="www/font")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="www/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="www/js")


# Run from command line
run(app, host='localhost', port=8081, debug=True)