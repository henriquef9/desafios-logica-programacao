

public class LongestPalindromicsubstring {

    public static void main(String[] args) {

        Solution s = new Solution();

        String result = s.longestPalindrome("cbbd");

        System.out.println(result);
    }

}


class Solution {
    public String longestPalindrome(String s) {

        int left_window = 0;
        int right_window = s.length() - 1;
        String polindrome = "";

        while(left_window < s.length()){

            while(right_window > left_window){

                int left = left_window;
                int right = right_window;

                while(left < right){

                    if(s.charAt(left) != s.charAt(right)){
                        break;
                    }

                    left++;
                    right--;

                }

                if(left >= right && polindrome.length() < (right_window - left_window + 1)){
                    polindrome = s.substring(left_window, right_window+1);
                }

                right_window--;
            }
            
            left_window++;
            right_window = s.length() - 1;
        }

        return polindrome;
    }
}