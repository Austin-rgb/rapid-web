import inspect
from html import *
from flask import Flask, request, make_response

def variable2str(string):
    pass
bootstrap_js = Script(attributes=dict(src='https://cdn.jsdelivr.net/npm/bootstrap@5.4.3/dist/js/bootstrap.bundle.min.js'))
bootstrap_css = Link(attributes=dict(rel='stylesheet',href='https://cdn.jsdelivr.net/npm/bootstrap@5.4.3/dist/css/bootstrap.min.css'))
        
def render(function, error = None):
    if callable(function):
        parameters = [param for param in inspect.signature(function).parameters]
        name = function.__name__.replace('_',' ').title()
        elements = []
        error_view = None
        if error:
            error_view = P(f'Invalid {error}')
        elements.append(Legend(name))
        for i in range(len(parameters)):
            if parameters[i] == error:
                elements.append(error_view)
            label = Label(parameters[i],{'for':parameters[i],'class':'form-label'})
            inp = Input(attributes={'id':parameters[i],'name':parameters[i]})
            div = Div(label,inp,attributes={'class':'mb-3'})
            elements.append(div)
        
        elements.append(Input(attributes={'type':'submit','value':name}))
        fieldset = Div(*tuple(elements),attributes={'class':'container'})
        form = Form(fieldset,attributes=dict(action=f'/{function.__name__}',method='post'))
        body = Body(form,bootstrap_js)
        head = Head(Title(name),bootstrap_css)
        html = Html(head,body)
        return html
        
    else:
        return render_api(function)
    
def render_api(api):
    elements = []
    api_attributes = dir(api)
    for attribute in api_attributes:
        if not attribute.startswith('__'):
            name = attribute.replace('_',' ').title()
            attr = getattr(api,attribute)
            if callable(attr):
                elements.append(A(name,attributes=dict(href=f'/{attribute}')))
                
            elif type(attr) == str:
                elements.append(P(name))
                elements.append(P(attr))
                
    div = Div(*tuple(elements))
    title = Title(type(api).__name__)
    head = Head(title)
    body = Body(div)
    html = Html(head, body)
    return html
    
def wrapper(api):
    def method():
        method_name = request.url.split('/')[-1]
        api_method = getattr(api,method_name)
        if request.method == 'GET':
            return render(api_method).generate()
            
        elif request.method == 'POST':
            params = inspect.signature(api_method).parameters.items()
            req_data = {}
            for param_name, param in params:
                cookie_value = request.cookies.get(param_name)
                if cookie_value:
                    req_data[param_name] = cookie_value
                    
                else:
                    if param.annotation == inspect._empty:
                        req_data [param_name] = request.form[param_name]
                        
                    try:
                        req_data[param_name] = param.annotation(request.form[param_name]) 
                        
                    except:
                        return render(api_method, error = param_name).generate()
            results = api_method(**req_data)
            resp = make_response(render(api).generate())
            resp.set_cookie(method_name,str(results))
            return resp
    return method
def api2flask_app(api):
    """
    creates a flask app that serves an api object 
    """
    
    # create flask instance
    app = Flask(__name__)
    
    # add full api rendering to the home route of the flask app
    app.add_url_rule('/','index',lambda: render(api).generate(),methods = ['GET'])

    # loop the methods of the api adding creating routes for them in the flask app
    for method_name in dir(api):
        # avoid adding routes for methods whose names start with '__'
        if not method_name.startswith('__') and callable(getattr(api, method_name)):
            
            method = wrapper(api)
            endpoint = '/' + method_name.replace('_', '/')
            app.add_url_rule(endpoint, method_name, lambda: method(),methods = ['GET','POST'])

    # return app ready to serve the api
    return app

class Demo:
    def __init__(self):
        self.welcome = '''
        Welcome dear devs, this is a demo api for testing Ochie's api_server package.
        Please feel free to contribute in our repository by suggesting features and posting issues.
        '''
        
    def add(self,number1:int=0,number2:int=0):
        return number1 + number2
        
    def mul(self,number1:int =0,number2:int=0):
        return number1 *number2
        
    def div(self,number1:int,number2:int):
        return number1/number2
        
demo = Demo()
app = api2flask_app(demo)
app.run(debug=True)
    