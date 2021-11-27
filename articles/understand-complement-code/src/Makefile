build:
	gcc -S foo.c
	gcc -c -Wa,-L foo.c

dump:
	objdump -d foo.o > dump.log

clear:
	rm foo.o foo.s