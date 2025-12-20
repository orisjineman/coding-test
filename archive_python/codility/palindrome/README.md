A string is a palindrome if it reads the same backward as forward.<br/>
For example, "madam" and "racecar" are palindromes, but "milk" is not.<br/>

Write a function:

`def solution(S)`

that, given a string S made of N letters, returns the maximum number of three-letter palindromes you can build using
letters from S. You can use each letter from S once.

Examples:

1. Given S = "aaaabc", the function should return 2.<br/>
   Examples of three-letter palindromes you can build simultaneously are "aba" and "aca".
2. Given S = "xyzwy", the function should return 1.
3. Given S = "dd", the function should return 0. You cannot build any three-letter palindrome.<br/>
4. Given S = "fknfkn", the function should return 2.<br/>

Write an efficient algorithm for the following assumptions:

* N is an integer within the range [1..50,000];
* string S is made only of lowercase letters (a-z)