def replace_o(word: str):
  if 'o' in word.lower():
    return word.lower().replace('o','%')
  else:
    return "Burts 'o' nav!"

if __name__=="__main__":
    print(replace_o("123231"))