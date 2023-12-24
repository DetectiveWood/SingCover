from mutagen import File

file = File('D:/Загрузки/Rick.mp3') # mutagen can automatically detect format and type of tags
artwork = file.tags['APIC:3.jpeg'].data
print(artwork)
with open('image.jpg', 'wb') as img:
   img.write(artwork) # write artwork to new imagefrom mutagen import File

file = File('D:/Загрузки/Rick.mp3') # mutagen can automatically detect format and type of tags
artwork = file.tags['APIC:3.jpeg'].data
print(artwork)
with open('image.jpg', 'wb') as img:
   img.write(artwork) # write artwork to new image