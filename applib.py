from peewee import *
import Random
import string

def random_string(self,length):
    letters = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters) for _ in range(length))
    return result
      
def hash(self,value):
    return hashlib.sha256(value.encode()).hexdigest()
    
def password_strength(password):
    strength = 0
    if len(password)>8:
        strength +=1
        
    for digit in string.digits:
        if digit in password:
            strength +=1
            break 
        
    for lower in string.ascii_lowercase:
        if lower in password:
            strength +=1
            break
            
    for upper in string.ascii_uppercase:
        if upper in password:
            strength +=1
            break
        
    for punctuation in string.punctuation:
        if punctuation in password: 
            strength +=1
            break
            
    return strength

db = SqliteDatabase('secure.db')
class User(Model):
    username = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db
        
class Session(Model):
    sessionId = CharField(unique =True)
    username = CharField()
    class Meta:
        database = db

class Permission(Model):
    destination = CharField()
    service = CharField()
    task = CharField()
    class Meta:
        database = db

class SecurityCallbacks:
    def __init__(self,username):
        self.callbacks = dict()
        
        
class PreLogin(Model):
    class Meta:
        database = db
        
class Prelogin(SecurityCallback):
    def __init__(self,sm,username):
        super().__init__(username)
        
        self.subscribed_callbacks = table.select(dict(username=username))
        
    def execute(self):
        state = True
        for key, value in self.callbacks:
            if key in self.subscribed_callbacks:
                state = state and self.subscribed_callbacks[key]()
                
        return state
        
    def add_callback(self,
        
class PostLogin(Model):
    class Meta:
        database = db
    
class Postlogin(SecurityCallbacks):
    def __init__(self):
        super().__init__()
        
    def execute(self):
        for key, value in self.callbacks:
            if key in self.subscribed_callbacks:
                state = state and self.subscribed_callbacks[key]()
        
class Secure: 
    
    def __init__(self,sm):
        self.security_callbacks = {}
        
    def add_callback(self,name, callback):
        self.security_callbacks[name] = callback
        
    def authenticate(self,username,password):
        user = User.get(User.username=username,password = self.hash(password))
        sessionId = None 
        prelogin = Prelogin(username)
        if user:
            if prelogin.execute(): sessionId = random_string(48)
            session = Session.get(Session.username=username, sessionId = sessionId )
            
        session.save()
        postlogin = Postlogin (username)
        postlogin.execute()
        return sessionId 
        
    def authorise(self,username,service_name,task_name):
        permission = Permission(destination=username, service =service_name,task = task_name)
        permission.save()
    
    def authenticated(self,sessionId):
        session = Session(sessionId=sessionId)
        if session: return True
        else: return False
        
    def authorised(self,service_name, task_name):
        session = Session(sessionId=sessionId)
        
        permission = Permission(username=self.username,service = service_name,task=task_name)
        if permission:return True 
        else: return False
