s = input("Enter one sentence :")

space_count = s.count(' ')

s_num = len(s) - space_count
average_length = s_num / (space_count+1)

print('average length of words:', average_length)


"""

sentence = input("Enter one sentence :")
space_count = sentence.count(' ') #띄어쓰기 주의
total = len(sentence) - space_count
average_length = total / (space_count+1)
print('average length of words:', average_length)


"""
