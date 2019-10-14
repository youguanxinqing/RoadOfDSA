#include "SingleLinked.h"

int main()
{
    List L = NULL;
    L = MakeEmpty(L);
    Insert(10, L, L);
    Insert(20, L, L->next);
    PrintLinked(L);

}