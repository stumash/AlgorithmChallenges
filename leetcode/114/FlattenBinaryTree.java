public class FlattenBinaryTree {
    public static void main(String[] args) {
        TreeNode t1 = new TreeNode(1);
        TreeNode t2 = new TreeNode(2);
        TreeNode t3 = new TreeNode(3);
        TreeNode t4 = new TreeNode(4);
        TreeNode t5 = new TreeNode(5);
        TreeNode t6 = new TreeNode(6);
        TreeNode t7 = new TreeNode(7);
        TreeNode t8 = new TreeNode(8);
        TreeNode t9 = new TreeNode(9);

        t1.left = t2;
        t2.left = t3;
        t3.right = t4;
        t2.right = t5;
        t1.right = t6;
        t6.left = t7;
        t6.right = t8;
        t8.right = t9;

        printTree(t1, 0);
        flatten(t1);
        printTree(t1, 0);
    }
    public static void printTree(TreeNode root, int depth)
    {
        for (int i = 0; i < depth; i++)
            System.out.print("    ");
        if (root == null)
        {
            System.out.println("-");
            return;
        }
        else
        {
            System.out.println(root.val);
            printTree(root.left, depth + 1);
            printTree(root.right, depth + 1);
        }
    }

    public static void flatten(TreeNode root)
    {
        if (root == null)
            return;

        flatten(root.right);

        if (root.left == null)
            return;

        flatten(root.left);
        endOfList(root.left).right = root.right;
        root.right = root.left;
        root.left = null;
    }
    public static TreeNode endOfList(TreeNode root)
    {
        while (root.right != null)
        {
            root = root.right;
        }
        return root;
    }
}

class TreeNode
{
    int val;
    TreeNode left;
    TreeNode right;
    public TreeNode(int x)
    {
        this.val = x;
    }
}
