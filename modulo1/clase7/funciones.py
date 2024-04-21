def deeper():
          print(' Now inside the function "deeper" ')
          
def deep():
          print(' Now inside the function "deep" ')
          deeper()
          print(' Now back inside the function "deep" ')
          
print(' Now inside the main program ')
deep()
print(' Now back inside the main program ')