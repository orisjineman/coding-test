public class BinarySearch {
    private static int binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length;

        while (end > start) {
            int mid = (start + end) / 2;
            int value = arr[mid];

            if (value == target) {
                return mid;
            } else if (value > target) {
                end = mid;  // down
            } else {
                start = mid + 1;    // up
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(binarySearch(new int[] {1, 3, 5, 7, 9}, 3)); // 1
        System.out.println(binarySearch(new int[] {1, 3, 5, 7, 9}, 9)); // 4
        System.out.println(binarySearch(new int[] {1, 3, 5, 7, 9}, 7)); // 3
        System.out.println(binarySearch(new int[] {1, 3, 5, 7, 9}, 10)); // -1
    }
}