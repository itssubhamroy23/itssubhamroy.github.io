//// Java program to check whether a
// string is a Palindrome using recursion
 
import java.io.*;
 
class GFG {
    public static boolean isPalindrome(int i, int j,
                                       String A)
    {
        // comparing the two pointers
        if (i >= j) {
            return true;
        }
 
        // comparing the characters on those pointers
        if (A.charAt(i) != A.charAt(j)) {
            return false;
        }
 
        // checking everything again recursively
        return isPalindrome(i + 1, j - 1, A);
    }
 
    public static boolean isPalindrome(String A)
    {
        return isPalindrome(0, A.length() - 1, A);
    }
 
    public static void main(String[] args)
    {
        // Input string
        String A = "geeks";
 
        // Convert the string to lowercase
        A = A.toLowerCase();
        boolean str = isPalindrome(A);
        System.out.println(str);
    }
}
