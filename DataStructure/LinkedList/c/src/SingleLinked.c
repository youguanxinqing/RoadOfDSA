#include "SingleLinked.h"

List MakeEmpty(List L)
{
    if (!L) {
        L = malloc(sizeof(struct Node));
        L->next = NULL;
    } else if (L->next != NULL) {
        DeleteList(L);
    }
    return L;
}

int IsEmpty(List L)
{
    if (!L) {
        return -1;
    } else if (!L->next) {
        return 1;
    } else {
        return 0;
    }
}

int IsLast(Position P)
{
    if (!P) {
        return -1;
    } else if (!P->next) {
        return 1;
    } else {
        return 0;
    }
}

Position Find(ElemType E, List L)
{
    Position P = NULL;

    if (L) {
        P = L->next;
        while (P && P->elem != E)
            P = P->next;
    }
    return P;
}

Position FindPrevious(ElemType E, List L)
{
    Position P = NULL;
    if (L) {
        P = L;
        while (P->next && P->next->elem != E)
            P = P->next;
    }
    return P;
}

void Delete(ElemType E, List L)
{
    Position P = FindPrevious(E, L);
    if (P) {
        Position tmpcell = P->next;
        P->next = P->next->next;
        free(tmpcell);
    }
}

void Insert(ElemType E, List L, Position P)
{
    Position ptr;
    
    if (!L) return;
    
    ptr = malloc(sizeof(struct Node));
    ptr->elem = E;
    ptr->next = NULL;

    ptr->next = P->next;
    P->next = ptr;
}

void DeleteList(List L)
{
    PtrNode tmpcell = NULL;
    while (L && L->next) {
        tmpcell = L->next;
        L->next = L->next->next;
        free(tmpcell);
    }
}

void PrintNode(Position P)
{
    if (P) {
        printf("%d\n", P->elem);
    } else {
        printf("%s\n", "nil");
    }
}

void PrintLinked(List L)
{
    if (L) {
        Position P = L->next;
        while (P) {
            printf("%d ", P->elem);
            P = P->next;
        }
        printf("\n");
    } else {
        printf("%s\n", "nil");
    }
}