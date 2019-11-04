#ifndef __BINART_SEARCH_TREE__
#define __BINART_SEARCH_TREE__

#include <stdio.h>
#include <stdlib.h>


#define true 1
#define false 0


type struct tree_node {
	int val;
	tree_node *left;
	tree_node *right;
} TreeNode;

/* 构建BST */
TreeNode *BuildBST(int[] arr);

/* 增删查 */
int InsertBST(TreeNode *T, int num);
int DeleteBST(TreeNode *T, int key);
int SearchBST(TreeNode T, int key, TreeNode *P);

/* 中序遍历 */
void TraverseBST(TreeNode *T, int[] arr);

#endif
