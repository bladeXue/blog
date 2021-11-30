import java.util.Arrays;

public class GetPermutation {

    private static int count = 0;
    private static int[] nums = { 0, 1, 2, 3, 4, 5, 6, 7 };

    private static void swap(int a, int b) {
        if (a < nums.length && b < nums.length) {
            int tmp = nums[a];
            nums[a] = nums[b];
            nums[b] = tmp;
        }
    }

    // nums[from] <-> nums[to]
    // to < len
    private static void reserve(int from, int to) {
        int offset = 0;
        while (offset < (to - from + 1) / 2) {
            swap(from + offset, to - offset);
            offset++;
        }
    }

    // boolean -> 是否找到了新的排列
    private static boolean getNextPermutation() {

        // 1. 找到第一个升序
        int len = nums.length;
        int i = len - 2;

        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
            if (i < 0)
                // 小于零说明已经找到全部排列
                return false;
        }
        // 2. 在右侧的降序中找最接近i的那个大数
        int j = len - 1;
        while (i < j && nums[i] >= nums[j]) {
            j--;
        }
        // 3. 交换升序数和最小大数
        swap(i, j);
        // 4.反转尾部字符串
        reserve(i + 1, len - 1);
        return true;
    }

    public static void main(String[] args) {

        System.out.println("the " + ++count + "th permutation: " + Arrays.toString(nums));

        int count2 = 20;
        while (getNextPermutation() && count2-- > 0) {
            System.out.println("the " + ++count + "th permutation: " + Arrays.toString(nums));
        }
    }
}