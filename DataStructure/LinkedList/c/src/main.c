#include <stdio.h>
#include <stdlib.h>

#include "SingleLinked.h"

int main() {
    printf( "init a list\n" );
    List L = NULL;
    L = MakeEmpty( L );
    
    printf( "insert 2, 1, 5, 10 : " );
    Position head = Header( L );
    Insert( 10, head, L );
    Insert( 5, head, L );
    Insert( 1, head, L );
    Insert( 2, head, L );
    PrintList( L );
    
    printf( "insert 9 after 1 : " );
    Position P1 = Find( 1, L );
    Insert( 9, P1, L );
    PrintList( L );

    printf( "delete 5 : " );
    Delete(5, L );
    PrintList( L );

    printf( "search elem before 10 : " );
    Position BeforeP10 = FindPrevious( 10, L );
    PrintNode(BeforeP10);
    printf( "is elem before 10 last : %d\n", IsLast(BeforeP10, L));
    
    printf( "is list empty : %d\n", IsEmpty( L ));
    printf( "clear linklist, " );
    DeleteList( L );
    printf( "output linklist content : " );
    PrintList( L );
    printf( "is list empty : %d\n", IsEmpty( L ));

}
