build:
	gcc -S foo.c
	gcc -c -Wa,-L foo.c

dump:
	objdump -d foo.o > dump.txt

clear:
	rm foo.o foo.s