'''
Copyright Sascha Spreitzer, 2014, GPLv2
'''

import sys
import StringIO

try:
    import pycurl
except:
    print "pycurl must be installed!"
    sys.exit(254)

class load(object):
    '''
    The load class, heart of webegg functions
    '''
    def __init__(self, url, namespace, ssl_verify=True):
        '''
        Initialize a webegg, an URL and namespace is needed
        ssl verification is optional but defaults to True
        '''
        self._url = url
        self._ns = namespace
        self._ssl_verify = ssl_verify
        self.load()
        
    def load(self):
        '''
        A wrapper function to call reload()
        '''
        self.reload()
    
    def reload(self):
        '''
        Loads code from URL, compiles and executes it in namespace
        '''
        buf = StringIO.StringIO()
        
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self._url)
        if self._ssl_verify:
            c.setopt(pycurl.SSL_VERIFYPEER, 1)
            c.setopt(pycurl.SSL_VERIFYHOST, 2)
        else:
            c.setopt(pycurl.SSL_VERIFYPEER, 0)
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.WRITEDATA, buf)
        c.perform()
        
        buf.seek(0)
        rcode = c.getinfo(pycurl.RESPONSE_CODE) 
        if rcode == 200:
            exec compile(buf.read(), "string", "exec") in self._ns
        else:
            raise Exception(str(rcode) + " HTTP Problem loading resource " + self._url)
        c.close()

class xload(object):
    '''
    The xload class, wraps to load arrays of resources from URL
    '''
    def __init__(self, url, items, namespace, ssl_verify=True):
        '''
        Initialize a webegg, an URL base, items and namespace is needed
        ssl verification is optional but defaults to True
        '''
        self._items = []
        for item in items:
            self._items.append(load(url + '/' + item + '.py', namespace, ssl_verify))
    
    def load(self):
        '''
        A wrapper function to call reload()
        '''
        self.reload()
        
    def reload(self):
        '''
        Reload every item, calls load.reload() of every item
        '''
        for item in self._items:
            item.reload()
