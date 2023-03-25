from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader( searchpath="templates/" )

#create the jinja2 environment
# env = 
#-tabnine next line-


env = Environment(loader=loader)

@app.route('/template', methods=['GET'])
def template():
    return render_response_from_env(env)
    #return render_template('template.html')
    #return render_template('template.html', name=name)
    


def render_response_from_env(env):
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

# Index page
@app.route('/')
def home():
    return render_response_from_env(env)