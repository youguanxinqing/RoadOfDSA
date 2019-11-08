#include <stdio.h>
#include <stdlib.h>

#include "bst.h"

SearchTree MakeEmpty( SearchTree T ) {
	if ( T ) {
		MakeEmpty( T->Left );
		MakeEmpty( T->Right );
		free( T );
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
			printf(" no enough memory ");
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
	SearchTree TmpCell;
	if ( !T ) return NULL;
	else if ( X < T->val ) T->Left = Delete( X, T->Left );
	else if ( X > T->val ) T->Right = Delete( X, T->Right );
	else if ( T->Left && T->Right) {
		TmpCell = FindMin( T->Right );
		T->val = TmpCell->val;
		T->Right = Delete( TmpCell->val, T->Right );
	}
	else {
		TmpCell = T;
		T = T->Left != NULL ? T->Left : T->Right ;
		free( TmpCell );
	}
	TmpCell = NULL;
	return T;
}

Element Retrieve( Position P ) {
	if ( P ) return P->val;
	else return -99999;

}

void InOrder( SearchTree T ) {
	if ( T ) {
		InOrder( T->Left );
		Element val = Retrieve( T );
		printf("%d ", val);
		InOrder( T->Right );
	}
}
