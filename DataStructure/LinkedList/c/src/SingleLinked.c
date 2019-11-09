#include <stdio.h>
#include <stdlib.h>

#include "SingleLinked.h"

#define FatalError printf

List MakeEmpty( List L ) {
    if ( !L ) {
        L = malloc( sizeof( struct Node ) );
        if ( !L )
            FatalError( "no enough memory" );
        L->Next = NULL;
    }
    else if ( L->Next )
        DeleteList( L );
    return L;
}

int IsEmpty( List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    return L->Next == NULL;
}

int IsLast( Position P, List L ) {
    if ( !P )
        FatalError( "unexpected null pointer\n" );
    return P->Next == NULL;
}

Position Find( Element X, List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    
    Position P = L->Next;
    while ( P ) {
        if ( X == P->val )
            break;
        P = P->Next;
    }
    return P;
}

Position FindPrevious( Element X, List L ) {
    Position P = NULL;
    while ( L && L->Next ) {
        if ( X == L->Next->val ) {
            P = L;
            break;
        }
        L = L->Next;
    }
    return P;
}

void Delete( Element X, List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    
    Position Tmp = NULL;
    Position P = FindPrevious( X, L );
    if ( P ) {
        Tmp = P->Next;
        P->Next = Tmp->Next;
        free( Tmp );
    }
}

void DeleteList( List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    
    Position Tmp = NULL, P = L->Next;
    while ( P ) {
        Tmp = P;
        P = P->Next;
        free( Tmp );
    }
    L->Next = NULL;
}

void Insert( Element X, Position P, List L ) {
    if ( !P )
        FatalError( "unexpected null pointer\n" );
    
    Position Tmp = malloc( sizeof( struct Node ) );
    if ( !Tmp )
        FatalError( "unexpected null pointer\n" );
    Tmp->val = X;
    Tmp->Next = P->Next;
    P->Next = Tmp;
}

Position Header( List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    return L;
}

Position First( List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    return L->Next;
}

Position Advance( Position P ) {
    if ( !P )
        FatalError( "unexpected null pointer\n" );
    return P->Next;
}

Element Retrieve( Position P ) {
    if ( !P )
        FatalError( "unexpected null pointer\n" );
    return P->val;
}

void PrintNode( Position P ) {
    if ( !P )
        FatalError( "unexpected null pointer\n" );
    printf( "%d\n", P->val );
}

void PrintList( List L ) {
    if ( !L )
        FatalError( "unexpected null pointer\n" );
    
    L = L->Next;
    while ( L ) {
        printf( "%d ", L->val );
        L = L->Next;
    }
    printf("\n");
}
