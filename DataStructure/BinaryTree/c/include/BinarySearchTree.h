#ifndef __BINART_SEARCH_TREE__
#define __BINART_SEARCH_TREE__

struct TreeNode;
typedef TreeNode *Position;
typedef TreeNode *SearchTree;
typedef int Element;

SearchTree MakeEmpty( SearchTree T );
Position Find( Element X, SearchTree T );
Position FindMin( Element X, SearchTree T );
Position FindMax( Element X, SearchTree T );
SearchTree Insert( Element X, SearchTree T );
SearchTree Delete( Element X, SearchTree T );
Element Retrieve( Position P );

#endif 

struct TreeNode {
    Element val;
    SearchTree Left, Right;
};
