package leetcode.java;

class TwoSum {
    public static void main(String[] args) {

        int arr[] = {2, 6, 5, 8, 11};
        int target = 14;

        int i, j, n;
        n = arr.length;
        for(i = 0; i < n; i++) {
            for(j = i+1; j < n; j++) {
                if (arr[i] + arr[j] == target) {
                    System.out.println("[" + i + ", " + j + "]");
                    return;
                }
            }
        }
    }
}