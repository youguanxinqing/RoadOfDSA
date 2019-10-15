TARGET = bin/app

CXX = gcc
SRC = src
OBJ = obj
OBJS =  $(OBJ)/main.o \
		$(OBJ)/SingleLinked.o

FLAGS += -Iinclude

vpath %.c src
vpath %.o obj
vpath %.h include

$(TARGET): $(OBJS)
	$(CXX) -o $@ $(OBJS)
$(OBJ)/main.o : main.c 
	$(CXX) -c $^ $(FLAGS) -o $@
$(OBJ)/SingleLinked.o : SingleLinked.c
	$(CXX) -c $^ $(FLAGS) -o $@


.PHONY : clean
clean:
	-rm $(TARGET) $(OBJS)
