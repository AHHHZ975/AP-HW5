def testArgv(*argv):  
    for arg in argv:  
        print(arg) 

def testKeyword(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  


testArgv('Hello', 'Welcome', 'to', 'AP', 'calss')  
testKeyword(first ='Hello', mid ='AP', last='Students') 