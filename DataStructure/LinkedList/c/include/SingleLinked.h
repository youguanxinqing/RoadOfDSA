#ifndef __SINGLELINKED_H__
#define __SINGLELINKED_H__

struct Node;
typedef struct Node *PtrToNode;
typedef PtrToNode List;
typedef PtrToNode Position;
typedef int Element;

List MakeEmpty( List L );
int IsEmpty( List L );
int IsLast( Position P, List L );
Position Find( Element X, Position P );
Position FindPrevious( Element X, Position P );
void Delete( Element X, List L );
void DeleteList( List L );
void Insert( Element X, Position P, List L );
Position Header( List L );
Position First( List L );
Position Advance( Position P );
Element Retrieve( Position P );
void PrintNode( Position P );
void PrintList( List L );

#endif

struct Node {
    Element val;
    Position Next;
};
