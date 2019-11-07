CXX = gcc

SRC = src
OBJ = obj
BIN = bin
INC = include


OBJS = $(addprefix $(OBJ)/, \
		 recursive_main.o \
		 bst.o \
		)

FLAGS += -Iinclude

vpath %.c $(SRC)
vpath %.o $(OBJ)
vpath %.h $(INC)

bin/recursive : $(OBJS)
	$(CXX) $^ -o $@

$(OBJ)/%.o : %.c
	$(CXX) -c $^ $(FLAGS) -o $@

.PHONY : clean config
config:
	-mkdir $(BIN) $(OBJ)

clean: 
	-rm $(BIN) $(OBJ) -rf
