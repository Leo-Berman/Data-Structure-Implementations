# Note that this make file uses "-g" to compile and link "debug".
#

# define a target for the application
#
all: nesteddict.exe

# define a target to link the application
#
nesteddict.exe: nesteddict.o
	g++ -g -lm nesteddict.o -o nesteddict.exe

# define targets to compile the source code
#
nesteddict.o: nesteddict.cpp Makefile
	g++ -g -c nesteddict.cpp -o nesteddict.o


# define a target to clean the directory
#
clean:
	rm -f nesteddict.o nesteddict.exe

#
# end of file
