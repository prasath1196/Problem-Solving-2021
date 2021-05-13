def sort_key(h):
  return h["max_index"]


def Anagrams(words,n):
  sorted_words = []
  grouped_words = []
  for word in words:
      sorted_words.append("".join(sorted(word)))
      store = {}
  for i in range(n):
      if sorted_words[i] in store.keys():
          res = store[sorted_words[i]]["res"] + [words[i]]
          store[sorted_words[i]] = {"max_index": i, "res": res }
      else: 
          store[sorted_words[i]] = {"max_index": i, "res": [words[i]]}
  for row in sorted(store.values(),key=sort_key):
    grouped_words.append(row["res"])
  return grouped_words





if __name__ == "__main__":
  words = ["act","god","cat","dog","tac"]
  res = Anagrams(words,5)
  print(res)