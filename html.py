class Element:
    def __init__(self,*elements,attributes:dict={}):
        self.elements = []
        self.inner_html = ''
        if len(elements)>0:
            if not type(elements[0]) == str:self.elements = list(elements)
            
            else:
                self.inner_html = elements[0]
        self.attributes = attributes
        self.attributes_str = ' '.join(f'{key}="{value}"' for key,value in attributes.items())
        self.is_container = False
        self.symbol = ''
        
    def insert(self,*args):
        self.elements.extend(list(args))
        
    def generate(self):
        html = '<'
        html += self.symbol
        html += ' ' + self.attributes_str
        if self.is_container:
            html += '>' + self.inner_html + '\n'.join(elem.generate() for elem in self.elements) + '</' + self.symbol + '>'
        else:
            html += '/>'
        return html

class A(Element):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'a'
        self.is_container = True
        
class Body(Element):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'body'
        self.is_container = True
        
class Button(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'button'
        self.is_container = True
        
class Div(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.symbol = 'div'
        self.is_container = True 
        
class Fieldset(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'fieldset'
        self.is_container = True
        
class Form(Element):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs) 
        self.symbol = 'form'
        self.is_container = True
        
class Head(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.symbol = 'head'
        self.is_container = True
        
        
class Html(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'html'
        self.is_container = True 
        
class Img(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'img'
        
        
class Input(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'input'
        
class Label(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'label'
        self.is_container = True
        
class Legend(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'label'
        self.is_container = True
        
class Link(Element):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'link'
        
class P(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.symbol = 'p'
        self.is_container = True 
        
class Script(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'script'
        self.is_container = True 
        
class Title(Element):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'title'
        self.is_container = True
        