package leetcode.java;

public class NestedLoopExample {
    public static void main(String[] args) {
        // Define the size of the multiplication table
        int size = 5;

        // Outer loop for rows
        for (int i = 1; i <= size; i++) {
            // Inner loop for columns
            for (int j = 1; j <= size; j++) {
                // Print the product of current row and column
                System.out.print(i * j + "\t");
            }
            // Move to the next line after each row
            System.out.println();
        }
    }
}
