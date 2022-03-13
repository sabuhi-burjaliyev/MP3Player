class MP3Player():
    def __init__(self,musiclist = []):
        self.musiclist = musiclist
        self.volume = 0
        self.status = True
        self.nowmusic = str()

    def showmenu(self):
        print("""
*****Welcome BS MP3Player *****
Your music list : {} 
The music playing now : {}
The volume : {}
1)Add music
2)Delete music
3)Turn down volume
4)Turn up volume
5)Change playing music
6)Exit   
""".format(self.musiclist,self.nowmusic,self.volume))

    def choicemenu(self):
        selection = int(input('Choose your option :'))
        while selection < 1 or selection >6:
            selection = int(input('Enter a number between (1-6) please !'))

        return selection

    def run(self):
        self.showmenu()
        selection = self.choicemenu()
        if selection == 1:
            self.addmusic()
        if selection == 2:
            self.deletemusic()
        if selection == 3:
            self.turndown()
        if selection == 4:
            self.turnup()
        if selection == 5:
            self.changemusic()
        if selection == 6:
            self.exit()
    def addmusic(self):
        groupname = input('Enter group or singer name :')
        musicname = input('Enter music name :')
        self.musiclist.append('{} - {}'.format(groupname,musicname))
    def deletemusic(self):
        counter = 1
        for music in self.musiclist:
            print('{}){}'.format(counter,music))
            counter += 1
        deletion = int(input('Enter the music will be deleted :'))
        while deletion < 1 or deletion > len(self.musiclist):
            deletion = int(input('Please enter a number between (1-{})'.format(len(self.musiclist))))
        self.musiclist.pop(deletion-1)
    def turndown(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 10
    def turnup(self):
        if self.volume == 100:
            pass
        else:
            self.volume += 10
    def changemusic(self):
        counter = 1
        for music in self.musiclist:
            print('{}){}'.format(counter,music))
            counter += 1
        selection = int(input('Enter the music number : '))
        while selection < 1 or selection > len(self.musiclist):
            selection = int(input('Enter a number between (1-{})'.format(len(self.musiclist))))
        self.nowmusic = self.musiclist[selection -1]
    def exit(self):
        self.status = False

mp3player = MP3Player()

while mp3player.status:
    mp3player.run()