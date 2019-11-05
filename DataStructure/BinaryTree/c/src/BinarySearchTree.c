#include <stdio.h>
#include <stdlib.h>
#include "BinarySearchTree.h"

SearchTree MakeEmpty( SearchTree T ) {
    if ( T ) {
        MakeEmpty( T->Left );
        MakeEmpty( T->Right );
        free( T );
    }
    return T;
}

Position Find( Element X, SearchTree T ) {
    if ( !T ) return NULL;
    else if ( X == T->val ) return T;
    else if ( X > T->val ) return Find( X, T->Right );
    else return Find( X, T->Left );
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
            printf("not enough memory\n");
            return NULL;
        }
        T->val = X;
        T->Left = T->Right = NULL;
        return T;
    } else if ( X == T->val ) {
        return T;
    } else if ( X > T->val ) {
        T->Right = Insert( X, T->Right );
    } else {
        T->Left = Insert( X, T->Left );
    }
    return T;
}

SearchTree Delete( Element X, SearchTree T ) {
    Position TmpCell;
    
    if ( !T ) return NULL;
    else if ( X > T->val ) T->Right = Delete( X, T->Right );
    else if ( X < T-> val ) T->Left = Delete( X, T->Left );
    else if ( T->Left && T->Right ) {
        TmpCell = FindMin( T->Right );
        T->val = TmpCell->val;
        T->Right = Delete( T->val, T->Right );
    } else {
        TmpCell = T;
        if ( T->Left ) T = T->Left;
        else if ( T-> Right ) T = T->Right;
        else T = NULL;
        free( TmpCell );
    }
    return T;
}

Element Retrieve( Position P ) {
    if ( P ) return P->val;
    return -999999;
}
