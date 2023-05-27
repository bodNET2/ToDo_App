from cffi import FFI

ffibuider = FFI()

ffibulider.cdef("void string_parse(int*, char*);")

ffibuilder.set_source("_tinput", 
    """
        #include "string_parse.h"
    """,
    sources = [string_parse.c],
    libraries = ["string"])

if __name__ == "__main__":
    ffibuilder.compile(verbose = True)