from flask import Flask

app = Flask(__name__)
default_name = 'Joe Bloggs'

@app.route('/')
def get_identiocn():
    name = default_name
    header = '<html><head><title>Identidock</title></head><doby>'
    body = '''<from method="POST">
            Hello <input type="text" name="name" value="{}">
            <input type="submit" value="submit">
            </form>
            <p> You look ike a:
            <img src="/monster/monster.png"/>
            '''.format(name)
    footer = '</body></html>'

    return header + body + footer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
