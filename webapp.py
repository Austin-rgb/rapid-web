class Document:
    def __init__(self,obj):
        self.obj = obj
        self.html = ''
        self.attribute_names = dir(obj)
        self.attributes = [obj.__getattribute__(name) for name in self.attribute_names]
        for i in range(len(self.attributes)):
            __class__ = self.attributes[i].__class__.__name__
            if __class__ =='builtin_function_on_method':
                self.add_method(i)
            elif __class__ =='str':
                self.add_label(i)
    def add_method(self,i):
        pass
        
    def html_form(labels=[],types=[],required=[]):
        pass