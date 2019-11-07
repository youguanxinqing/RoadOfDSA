#include <stdio.h>
#include <stdlib.h>

#include "bst.h"

int main() {
	SearchTree tree = NULL;
	tree = Insert( 10, tree );
	tree = Insert( 1, tree );
	tree = Insert( 7, tree );
	tree = Insert( 15, tree );
	tree = Insert( 6, tree );
	tree = Insert( 11, tree );

	printf( "in order :" );
	InOrder( tree );
	printf( "\n" );

	Position p_min = FindMin( tree );
	printf( "min element is %d \n", Retrieve(p_min) );

	printf( "delete element 7 : " );
	tree = Delete( 7, tree );
	InOrder( tree );
	printf("\n");

	printf( "insert element 8 : " );
	tree = Insert( 8, tree );
	InOrder( tree );
	printf( "\n" );
	
	Position p_max = FindMax( tree );
	printf( "max element is %d\n", Retrieve(p_max) );

	printf( "find element 16 : " );
	Position p16 = Find( 16, tree );
	if ( p16 ) {
		printf( "exits (%d) \n", Retrieve(p16) );
	} else {
		printf( "no exits \n" );
	}

	printf( "find element 6 : " );
	Position p6 = Find( 6, tree );
	if ( p6 ) {
		printf( "exits (%d) \n", Retrieve(p6) );
	} else {
		printf( "no exits \n" );
	}

	printf( "clear tree : " );
	tree = MakeEmpty( tree );
	if ( tree ) {
		InOrder( tree );
		printf( "\n" );
	} else {
		printf( "tree is null\n" );
	}
}
