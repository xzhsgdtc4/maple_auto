import datetime,threading, time



def repeat(i,j,k = 1 ):
    print('This is foo',i,j,' ',datetime.datetime.now())
    threading.Timer(i, repeat).start()


# def my_decorator(some_function):

#     def wrapper():

#         threading.Timer(1,some_function).start()

#         print("Something is happening after some_function() is called.")

#     return wrapper



# @my_decorator
# def print_time():
# 	print(time.time())


repeat(1,0)
repeat(2,1)

print('do something else')