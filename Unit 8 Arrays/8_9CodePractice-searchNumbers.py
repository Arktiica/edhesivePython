def search(a):
  for i in range(len(v)):
    if (v[i] == a):
      print(i)
      return
  print("-1")


v = [24, 20, 29, 32, 34, 29, 49, 46, 39, 23, 42, 24, 38]

msg = int(input("Search for: "))

search(msg)
