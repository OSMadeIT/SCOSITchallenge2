socks = [12,12,12,12,14,16,45,45,67]
pairs = []
for i in socks:
  if socks.count(i) > 1:
    pairs.append(i)
    print(pairs)
    for j in pairs:
      sell = pairs.count(j) // 2
      print(sell)
