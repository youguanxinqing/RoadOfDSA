#include "BinarySearchTree.h"


TreeNode *BuildBST(int[] arr) {
	malloc()
}

int InsertBST(TreeNode *T, int num) {
	
	if (!T) {
		TreeNode *n = malloc(sizeof(TreeNode))
		n->val = num;
		n->left = n->right = NULL;
		T = n;
		return true;
	} else if (T->val == num) {
		return false;
	} else if (T->val < num) {
		InsertBST(T->left, num);
	} else {
		InsertBST(T->right, num);
	}

}
