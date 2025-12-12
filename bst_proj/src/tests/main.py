from src.bst.tree import BinarySearchTree

def main():
    bst = BinarySearchTree()
    
    print("inserting elements...")
    bst.insert(50, "Root")
    bst.insert(30, "Left")
    bst.insert(70, "Right")
    bst.insert(20, "Left-Left")
    bst.insert(40, "Left-Right")
    bst.insert(60, "Right-Left")
    bst.insert(80, "Right-Right")
    
    print("\nSearching elements...:")
    print("Key 40:", bst.search(40))
    print("Key 90:", bst.search(90))
    
    print(f"\nTree height: {bst.height()}")
    
    print(f"\nTree balanced: {bst.is_balanced()}")
    
    print(f"\nInorder traversal: {bst.inorder_traversal()}")
    
    print("\nDeleting key 30...")
    bst.delete(30)
    print(f"Inorder travers. after deletion: {bst.inorder_traversal()}")
    print(f"Tree height afrer deletion: {bst.height()}")
    
    print("\nCreating imbalanced tree...")
    unbalanced_bst = BinarySearchTree()
    for i in range(1, 6):
        unbalanced_bst.insert(i, f"Value{i}")
    
    print(f"Height: {unbalanced_bst.height()}")
    print(f"Balanced: {unbalanced_bst.is_balanced()}")

if __name__ == "__main__":
    main()