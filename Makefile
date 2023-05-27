par_compile:
	gcc -c -g string_parse.c -o string_parse.o 
shared_lib: string_parse.o
	gcc -fPIC -shared string_parse.o -o string_parse.so 
