#include <stdio.h>
#include <stdlib.h>

#include "bst.h"

SearchTree MakeEmpty( SearchTree T ) {
	if (T) {
		MakeEmpty( T->Left );
		MakeEmpty( T->Right );
		free(T);
		T = NULL;
	}
	return T;
}

Position Find( Element X, SearchTree T ) {
	if ( !T ) return NULL;
	else if ( X == T->val ) return T;
	else if ( X < T->val ) return Find( X, T->Left );
	else return Find( X, T->Right );
}

Position FindMin( SearchTree T ) {
	if ( !T ) return NULL;
	else if ( !T->Left ) return T;
	else return FindMin( T->Left );
}

Position FindMax( SearchTree T ) {
	if ( !T ) return NULL;
	else if ( !T->Right ) return T;
	else return FindMax( T->Right );
}

SearchTree Insert( Element X, SearchTree T ) {
	if ( !T ) {
		T = malloc( sizeof( struct TreeNode ) );
		if ( !T ) {
			printf("not enough memory");
			return NULL;
		}
		T->val = X;
		T->Left = T->Right = NULL;
	} 
	else if ( X < T->val ) T->Left = Insert( X, T->Left );
	else if ( X > T->val ) T->Right = Insert( X, T->Right );
	return T;
}

SearchTree Delete( Element X, SearchTree T ) {
	Position TmpCell;
	
	if ( !T ) return NULL;
	else if ( X < T->val ) T->Left = Delete( X, T->Left );
	else if ( X > T->val ) T->Right = Delete( X, T->Right );
	else if ( T->Left && T->Right ) {
		TmpCell = FindMin( T->Right );
		T->val = TmpCell->val;
		T->Right = Delete( TmpCell->val, T->Right );
	} 
	else {
		TmpCell = T;
		T = T->Left != NULL ? T->Left : T->Right;
		free( TmpCell );
	}
	return T;
}


void InOrder( SearchTree T ) {
	if ( T ) {
		InOrder( T->Left );
		printf("%d ", T->val);
		InOrder( T->Right );
	}
}

void main() {
	// test insert
	SearchTree tree = NULL;
	tree = Insert(10, tree);
	tree = Insert(2, tree);
	tree = Insert(11, tree);
	tree = Insert(1, tree);

	InOrder( tree );
	printf("\n");

	// test delete
	Delete( 10, tree );
	InOrder( tree );
	printf("\n");

	// test find
	Position target = Find(3, tree);
	if ( !target ) printf("no the node\n");
	else printf("%d\n", target->val);

	// test min
	Position min = FindMin( tree );
	if ( !min ) printf("tree is null\n");
	else printf("%d\n", min->val);

	// test max
	Position max = FindMax( tree );
	if ( !max ) printf("tree is null \n");
	else printf("%d\n", max->val);

	tree = MakeEmpty( tree );
	if ( !tree ) printf("tree is null \n");
	else printf("tree is not null\n");
}
