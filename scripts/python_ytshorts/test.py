import os
def upload(country):
    country=country.upper()
    filepath="C:\\python_ytshorts\\static\\temp.mp4"
    title=str("\"AMAZING LIFE FACT about {} #shorts\"").format(country)
    description="\"ABOUT OUR CHANNEL Our channel is about Facts. We cover lots of cool stuff such as Facts Check out our channel here:https://www.youtube.com/channel/UCeT_1wHgBWVfNZUM4tCWWmADon’t forget to subscribe!\""
    keywords=str("\"facts about the {},facts about,facts about {},amazing facts about {},surprising facts about the {},5 random facts about the {},about,interesting facts about {},random facts about the {},the worst things about {},facts about beer,facts about skoda,facts about czech,facts about czechs,facts about the world,facts about countries,facts about ice hockey\"").format(country.lower(),country.lower(),country.lower(),country.lower(),country.lower(),country.lower(),country.lower(),country.lower())
    status= "\"public\""
    category= "\"1\""

    cmd="python upload.py --file={} --title={}  --description={} --category={} --keywords={} --privacyStatus={} ".format(filepath,title,description,category,keywords,status)
    print(cmd)
    os.system(cmd)


    

