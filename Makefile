CC= gcc
CFLAGS= -g -Wall -std=c99 -pedantic-errors
INCLUDES =
LFLAGS =
LIBS = -lm

MAIN= echo_byte
SRCS= echo_byte.c timer.c print_tools.c
OBJS= $(SRCS:.c=.o)

.PHONY: depend clean

all:$(MAIN)
	@echo  Listo

$(MAIN):$(OBJS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS) $(LFLAGS) $(LIBS)

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o $(MAIN)

# DO NOT DELETE THIS LINE -- make depend needs it
