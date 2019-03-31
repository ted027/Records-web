import boto3
import time
import functools
import collections

# https://wiki.python.org/moin/PythonDecoratorLibrary#Cached_Properties
class cached_property(object):
    '''Decorator

    '''

    def __init__(self, ttl=300):
        self.ttl = ttl

    def __call__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        return self

    def __get__(self, inst, owner):
        now = time.time()
        try:
            value, last_update = inst._cache[self.__name__]
            if self.ttl > 0 and now - last_update > self.ttl:
                raise AttributeError
        except (KeyError, AttributeError):
            value = self.fget(inst)
            try:
                cache = inst._cache
            except AttributeError:
                cache = inst._cache = {}
            cache[self.__name__] = (value, now)
        return value

# https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
   '''Decorator.

   '''

   def __init__(self, func):
      self.func = func
      self.cache = {}

   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value

   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__

   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

class AwsInit(object):
    def __init__(self):
        self.__region = None
        self.__profile = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, x):
        self.__region = x

    @property
    def profile(self):
        return self.__profile

    @profile.setter
    def profile(self, x):
        self.__profile = x

    @memoized
    def __call__(self, service_name, endpoint=None, region=None, profile=None):
        return AwsService(service_name, region=region or self.region, endpoint=endpoint or None, profile=profile or self.profile)

class AwsService(object):
    def __init__(self, service_name, region=None, endpoint=None, profile=None):
        self.__service_name = service_name
        self.__region = region
        self.__endpoint = endpoint
        self.__profile = profile

    @cached_property(ttl=0)
    def session(self):
        return boto3.Session(region_name=self.__region, profile_name=self.__profile)

    @cached_property(ttl=0)
    def resource(self):
        return self.session.resource(self.__service_name, endpoint_url=self.__endpoint)

    @cached_property(ttl=0)
    def client(self):
        try:
            return self.resource.meta.client
        except:
            return self.session.client(self.__service_name, endpoint_url=self.__endpoint)
