#include "BinarySearchTree.h"

SearchTree Insert(Element E, SearchTree T) {
    
    if (!T) {
        T = malloc(sizeof(struct TreeNode));
        T->E = E;
        T->Left = T->Right = NULL;
    } else if (T->E == E) {
        return T; 
    } else if (T->E < E) {
        T->Right = Insert(E, T->Right);
    } else {
        T->Left = Insert(E, T->Left);
    }

    return T;
}
