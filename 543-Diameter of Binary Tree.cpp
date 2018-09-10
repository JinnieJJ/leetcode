/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root)
            return 0;
        int leftPart = 0, rightPart = 0, leftHeight = 0, rightHeight = 0;
        if (root->left){
            leftPart = diameterOfBinaryTree(root->left);
            leftHeight = getMaxHeight(root->left);
        }           
        if (root->right){
            rightPart = diameterOfBinaryTree(root->right);
            rightHeight = getMaxHeight(root->right);
        }
        return max(max(leftPart, rightPart), leftHeight + rightHeight);    
    }
    int getMaxHeight(TreeNode *root) {
        if (!root)
            return 0;
        int maxLeft = 0, maxRight = 0;
        if (root->left) 
            maxLeft = getMaxHeight(root->left);
        if (root->right)
            maxRight = getMaxHeight(root->right);        
        return max(maxLeft, maxRight) + 1;
    }
};
