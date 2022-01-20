class Singleton:
  instance=None

  @staticmethod
  def get_obj():
     if Singleton.instance:
        return Singleton.instance
     else:
        Singleton.instance=Singleton()
  def __init__(self):
      if Singleton.instance:
         raise Exception("Cannot instantiate Twice")    
      else:
         self.a=0
         self.b=0
         Singleton.instance=self

  @property
  def get_a(self):
      return self.a

  @get_a.setter
  def get_a(self,a):
      self.a=a
      return self.a

  @property
  def get_b(self):
     return self.b

  @get_b.setter
  def get_b(self,b):
      self.b=b
      return self.b

if __name__=="__main__":
   a=Singleton()
   a.get_a=4
   a.get_b=5
   print(a.__dict__)
   try:
     b=Singleton()
   except Exception as e:
     b=Singleton.get_obj()
     print(b.__dict__)
        
        