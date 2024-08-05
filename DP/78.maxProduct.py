# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/


class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(s: str) -> bool:
            # Check if the string `s` reads the same forwards and backwards
            return s == s[::-1]

        def generate_palindromic_subsequences(s: str) -> list:
            # Get the length of the string `s`
            n = len(s)
            # Initialize an empty list to store palindromic subsequences and their bitmasks
            palindromes = []

            # Iterate over all possible subsets of the string using bitmasking
            for mask in range(1, 1 << n):
                # Initialize an empty string to build the current subsequence
                subseq = ""
                # Iterate through each bit position in the mask
                for i in range(n):
                    # Check if the i-th bit in the mask is set (i.e., if the character at index i should be included)
                    if mask & (1 << i):
                        subseq += s[i]  # Add the character at index i to the subsequence
                # Check if the generated subsequence is a palindrome
                if is_palindrome(subseq):
                    # If it is a palindrome, store it along with its bitmask
                    palindromes.append((subseq, mask))

            # Return the list of palindromic subsequences and their bitmasks
            return palindromes

        def max_palindromic_product(s: str) -> int:
            # Generate all palindromic subsequences and their bitmasks
            palindromes = generate_palindromic_subsequences(s)
            # Initialize a variable to keep track of the maximum product of lengths found
            max_product = 0
            # Get the total number of palindromic subsequences
            num_palindromes = len(palindromes)

            # Compare each pair of palindromic subsequences to find the maximum product
            for i in range(num_palindromes):
                for j in range(i + 1, num_palindromes):
                    s1, mask1 = palindromes[i]  # First subsequence and its bitmask
                    s2, mask2 = palindromes[j]  # Second subsequence and its bitmask
                    # Check if the two subsequences are disjoint (i.e., their bitmasks do not overlap)
                    if mask1 & mask2 == 0:
                        # Calculate the product of the lengths of the two disjoint subsequences
                        product = len(s1) * len(s2)
                        # Update the maximum product if the current product is greater
                        max_product = max(max_product, product)

            # Return the maximum product found
            return max_product

        # Call the method to calculate the maximum product of palindromic subsequences
        return max_palindromic_product(s)
