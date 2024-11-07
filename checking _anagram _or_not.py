word_1=input('enter any word to anagram or not ::')
word_2=input('enter any word to anagram or not ::')
def anagram_or_not(word_1,word_2):
  if len(word_1)==len(word_2) and sorted(word_1)==sorted(word_2):
    return True
  else:
    return:False
