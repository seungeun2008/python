

#if문 성별,나이 구분


a = int(input("나이:"))
b = input("성별:")

if  a <= 19 and b == "여자":
      print("girl")
elif a >19 and b == "여자":
      print("woman")
elif a <= 19 and b == "남자":
      print("boy")
elif a > 19 and b == "남자":
      print("man")
