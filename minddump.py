mind_dump = []
print("So what's on your mind for today? ")
print("Common, you don't need to pen and paper to write it. Type it here:")
print("Type GOT IT once done dumping things off")
while True:
    new_item = input("- ")
    if new_item == 'GOT IT':
        break
    mind_dump.append(new_item)

print("Here are your footprints to follow up for the day:")
for dump in mind_dump:
    print(dump)
