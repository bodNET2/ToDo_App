import ctypes
import os
import time

path = os.getcwd()
C_library = ctypes.CDLL( os.path.join(path,"string_parse.so") )

time_parse = C_library.string_parse
time_parse.argtypes = [(ctypes.c_int * 3), ctypes.c_char_p]

# def time_input(timer):
#    out  = (ctypes.c_int * 3)(0,0,0)
#    time_parse( out, timer.encode())
#    return list(out)

# kin = input("Enter a time:")
# start = time.time()
# m = time_input(kin)
# end = time.time()
# print(end-start)
# print(m)