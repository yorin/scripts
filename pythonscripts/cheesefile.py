import datetime
#http://stackoverflow.com/questions/5453331/adding-to-a-date-checking-if-past-expiration-date
class Date(object):
    def __init__(self, s):
        if isinstance(s, Date):
            self.date = s.date
        elif isinstance(s, datetime.date):
            self.date = s
        else:
            self.date = datetime.datetime.strptime(s, "%d/%m/%Y")

    def __add__(self, val):
        if isinstance(val, Life):
            val = val.life
        elif not isinstance(val, datetime.timedelta):
            val = datetime.timedelta(val)
        return self.__class__(self.date + val)

    def __cmp__(self, val):
        return (self.date - val.date).days

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

class Life(object): 
    def __init__(self, s):
        if isinstance(s, Life):
            self.life = s.life
        elif isinstance(s, datetime.timedelta):
            self.life = s
        else:
            self.life = datetime.timedelta(days=int(s))

    def __str__(self):
        return str(self.life.days)

class Product(object):
    FMT = "{0:10} {1:10} {2:24}".format

    def __init__(self, date, life, name):
        super(Product,self).__init__()
        self.date = Date(date)
        self.life = Life(life)
        self.name = str(name).strip()

    def __str__(self):
        return Product.FMT(self.date, self.life, self.name)

    def expires(self):
        return Date(self.date + self.life)

    @classmethod
    def get(cls):
        date = getClass(Date, "Please enter the date (DD/MM/YYYY): ")
        life = getClass(Life, "Please enter the life (in days): ")
        name = raw_input("Please enter the name of the cheese: ")
        return cls(date, life, name)

    def vals(self):
        return self.date, self.life, self.name

class FileOf(object):
    def __init__(self, cls):
        self.data = {}
        self.cls  = cls

    def loadFile(self, fname, mode='r', sep=':'):
        _data = self.data
        _cls  = self.cls
        with open(fname, mode) as inf:
            for line in inf:
                try:
                    items = line.strip().split(sep)
                    id = items.pop(0)
                    _data[id] = _cls(*items)
                except ValueError, e:
                    print(e)
        return self

    def saveFile(self, fname, mode='w', sep=':', eol='\n', key=None):
        _data = self.data
        keys = _data.keys()
        keys.sort(key=key)
        with open(fname, mode) as outf:
            for id in keys:
                outf.write(str(id)+sep)
                outf.write(sep.join(str(v) for v in _data[id].vals()))
                outf.write(eol)
        return self

    def addNew(self):
        id  = getNewKey(self.data, "Please enter the new ID: ")
        obj = getClass(self.cls)
        self.data[id] = obj
        return self

    def printAll(self, key=None):
        _data = self.data
        _cls  = self.cls
        ID = "{0:4} ".format
        print ID("id") + _cls.FMT("Date", "Life", "Name")
        keys = _data.keys()
        keys.sort(key=key)
        for id in keys:
            print ID(id) + _cls.FMT(*(_data[id].vals()))
        return self

    def filter(self, filterFn):
        newFile = FileOf(self.cls)
        newFile.data = {id:item for id,item in self.data.iteritems() if filterFn(id, item)}
        return newFile

def getNewKey(keys, msg='', keytype=str):
    "Prompt for a key not already in keys"
    while True:
        key = keytype(raw_input(msg))
        if key in keys:
            print("This key already exists. Please try again.")
        else:
            return key

def getClass(cls, *args, **kwargs):
    "Return a new instance of given class; prompt for required values"
    if hasattr(cls, 'get'):
        # if the class knows how to 'get' itself, let it
        return cls.get(*args, **kwargs)
    else:
        # otherwise we assume the class knows how to init itself from a string
        while True:
            s = raw_input(*args)
            try:
                return cls(s, **kwargs)
            except ValueError, e:
                print(e)

def getExpired(cheeses, asOf=None):    
    asOf = Date(asOf) if asOf else getClass(Date, "Please enter expiration test date (DD/MM/YYYY): ")
    return cheeses.filter(lambda id,obj: obj.expires() <= asOf)

def main():
    cheeses = FileOf(Product).loadFile('cheesefile.txt')
    cheeses.printAll()

    cheeses.addNew()

    expiredA = getExpired(cheeses)                 # prompt for expiration date
    expiredB = getExpired(cheeses, "12/3/2011")    # use given date

    print("The expired items are:")
    expiredB.printAll()

    cheeses.saveFile('cheesefile.txt')

if __name__=="__main__":
    main()

