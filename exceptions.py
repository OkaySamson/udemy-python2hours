print("hello")

try:
    import blahblah
except Exception:
    print("this requested module is under maintainance")

try:
    import blahblah
except ImportError:
    print("this requested module is under maintainance")


try:
    #try to see whether this gives an exception
    import dc
except Exception:
    #if there is an exception throw this message
    print("this requested module is under maintainance")
else:
    print(dc.companyName)
    #if there is no exception then execute this code
    


print("world")