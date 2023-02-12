table = []
for j in range(32):
    table.append([chr(1039 + i % 1071) if i > 1071 else chr(i) for i in range(1040+j, 1072+j)])
for i in table:
    print(i)
