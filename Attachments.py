import requests

class SaveAttachment:
    def __init__(self, url):
        self.url = url
        self.r = requests.get(self.url, allow_redirects=True)

    def save_file(self, url):
        self.name = self.url.split("/")[-1:]
        return open("".join(self.name), "wb").write(self.r.content)
        
#Get the attachment from a URL
url = 'https://dl.airtable.com/.attachments/df34772226061257eb7ed599cda373f0/2405a5a2/WertgarantieMarzo.png'
r = requests.get(url, allow_redirects=True)

#Get the name of the file by extracting the last part of the URL
name = url.split("/")[-1:]

#Remove unnecesary characters from the name while
#Save the file in the same directory
open("".join(name), "wb").write(r.content)