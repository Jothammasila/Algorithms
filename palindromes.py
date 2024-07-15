def palindrome_checker(word: str) -> str:
   word = word.lower()
   for i in range(len(word)):
       if word[i] == word[-i - 1]:
           return f"\'{word.capitalize()}\' is a palindrome."
       else:
           return f"\'{word.capitalize()}\' is not a palindrome."