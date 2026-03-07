with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Delete lines 985 to 1064 (0-indexed 984 to 1064)
del lines[984:1064]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Deleted broken script block')
