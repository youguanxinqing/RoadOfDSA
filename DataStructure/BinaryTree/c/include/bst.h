#ifndef __BST_H__
#define __BST_H__

struct TreeNode;
typedef struct TreeNode *Position;
typedef struct TreeNode *SearchTree;
typedef int Element;

SearchTree MakeEmpty( SearchTree T );

Position Find( Element X, SearchTree T );
Position FindMin( SearchTree T );
Position FindMax( SearchTree T );

SearchTree Insert( Element X, SearchTree T );
SearchTree Delete( Element X, SearchTree T );

Element Retrieve( Position P );
void InOrder( SearchTree T );

#endif

struct TreeNode {
	Element val;
	SearchTree Left, Right;
};
