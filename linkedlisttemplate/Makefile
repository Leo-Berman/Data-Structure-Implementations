# Note that this make file uses "-g" to compile and link "debug".
#

# define a target for the application
#
all: linkedlisttemplate.exe

# define a target to link the application
#
linkedlisttemplate.exe: linkedlisttemplate.o
	g++ -g -lm linkedlisttemplate.o -o linkedlisttemplate.exe

# define targets to compile the source code
#
linkedlisttemplate.o: linkedlisttemplate.cpp Makefile
	g++ -g -c linkedlisttemplate -o linkedlisttemplate.o


# define a target to clean the directory
#
clean:
	rm -f linkedlisttemplate.o linkedlisttemplate.exe

#
# end of file
