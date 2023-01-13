import matplotlib.pyplot as plt

#This script can be used to find how many times a particular word is used and by which user.
#This can be particularly userful for a group conversation,just for fun😁

filename = input('Enter the file Name : ')

#Ensure the file is in same path to the script
#or you can enter path to the file

word_to_find = input('which word you want to find? :')


chat = open(str(filename), 'r', encoding='utf_8')
data = chat.readlines()
Names_duplicate = []

for n in range(1, 2000):

    start = data[n].find('-')
    end = -1
    occurrence = 2
    for i in range(0, occurrence):
        end = data[n].find(':', end + 1)
    name = data[n][start+1:end]
    Names_duplicate += [name]


Names = []
for i in Names_duplicate:
    if i not in Names and i.startswith(' '):
        Names.append(i)

count = []
for i in Names:
    rep = 0
    for j in data:
        if str(j.find(str(word_to_find))) != '-1' and str(j.find(i)) != '-1':
            rep = rep + 1
    count.append(i)  
    count.append(rep)
textfile = open("a_file.txt", "w")
for element in count:
    textfile. write(str(element)+'\n')

textfile.close()

plot_Name = []
plot_instances = []
plot_data = {}
for i in range(0, len(count)-1):
    if i % 2 == 0:
        plot_Name.append(count[i])
    if i % 2 != 0:
        plot_instances.append(count[i])

for plot in range(0, 16):
    plot_data[plot_Name[plot]] = plot_instances[plot] 
x = list(plot_data.keys())
y = list(plot_data.values())
fig = plt.figure(figsize=(400, 5))

plt.bar(x, y)
plt.show()
