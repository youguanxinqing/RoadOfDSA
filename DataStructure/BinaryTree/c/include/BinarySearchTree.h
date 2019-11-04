#ifndef __BINART_SEARCH_TREE__
#define __BINART_SEARCH_TREE__

#include <stdio.h>
#include <stdlib.h>

struct TreeNode;
typedef struct TreeNode *Position;
typedef struct TreeNode *SearchTree;
typedef int Element;

SearchTree MakeEmpty(SearchTree T);
Position Find(Element E, SearchTree T);
Position FindMin(SearchTree T);
Position FindMax(SearchTree T);
SearchTree Insert(Element E, SearchTree T);
SearchTree Delete(Element E, SearchTree T);
Element Retrive(Position T);

#endif

struct TreeNode {
    Element E;
    SearchTree Left, Right;
};
