CXX = gcc

SRC = src
OBJ = obj
BIN = bin
INC = include
TARGET = $(BIN)/app

OBJS = $(addprefix $(OBJ)/, \
		 main.o \
		 SingleLinked.o \
		)

FLAGS += -Iinclude

vpath %.c $(SRC)
vpath %.o $(OBJ)
vpath %.h $(INC)


$(TARGET): $(OBJS)
	$(CXX) $^ -o $@

$(OBJ)/%.o : %.c
	$(CXX) -c $^ $(FLAGS) -o $@


.PHONY : clean pre
config:
	-mkdir $(BIN) $(OBJ)
clean:
	-rm ./bin ./obj -rf
