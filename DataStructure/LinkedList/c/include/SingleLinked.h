#ifndef _single_linked_h_
#define _single_linked_h_

#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;

struct Node;
typedef struct Node *PtrNode;
typedef PtrNode List;
typedef PtrNode Position;

List MakeEmpty(List L);
int IsEmpty(List L);
int IsLast(Position P);
Position Find(ElemType E, List L);
void Delete(ElemType E, List L);
Position FindPrevious(ElemType E, List L);
void Insert(ElemType E, List L, Position P);
void DeleteList(List L);
void PrintNode(Position P);
void PrintLinked(List L);

struct Node {
    ElemType elem;
    PtrNode next;
};

#endif