s = " xue peng cheng '"
print(s.strip().rstrip('\'').lstrip())


s1 = s
s = "peng cheng xue"
print(s.strip())
print(s1);


print(s.index('peng'))


s2 = "cheng"
print(cmp(s,s2))