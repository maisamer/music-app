import sqlite3 as lite
import time
conn = lite.connect('appssongss.db')

##############start of class band ###################
class band:
    def __init__(self,bandname):
         if bandname!=0:
           self.bandname=bandname #string
           f=True
           with conn:
                cur = conn.cursor()
                find=cur.execute("SELECT  name FROM artist   where bandname = ?", (bandname,))
                for row in find:
                    print(row[0])
                    if row[0] != None:
                       f=False
                       break
           if f == True:   
                 with con:
                      cur = con.cursor()    
                      cur.execute("INSERT INTO band(name) VALUES (?) ", (bandname,))
           else:
               print("this band is already in database")          
##############end of class band

########### class artist ##############
class Artist:
    def __init__(self, name=0, dateofbirth=0 , bandname=0):
      if name !=0:
        self.name = name
        self.dateofbirth = dateofbirth
        self.bandname = bandname
        
    def view_all(self):
        with conn:
            cursor = conn.execute("SELECT name from Artist")
        for row in cursor :
            print ("name = ", row[0])
        print('######################################################')
    def view_artist(self,name):#check
        #individual songs
        with conn:
            cur = conn.cursor()
            cursor = cur.execute("SELECT name,length from  song  WHERE featuredartist=? ",(name,))
        print(name)
        for row in cursor :
            print ("song name : ", row[0]," length : ",row[1])
        #band song
        with conn:
            cur = conn.cursor()
            cursor = cur.execute("SELECT name,length  FROM  artistInBand  INNER JOIN song  ON artistInBand.bandName = song.bandName where artistName = ?", (name,))
        for row in cursor:
            print ("song name : ", row[0]," length : ",row[1])
        print('######################################################')
    def add_artist(self,name=0,dateofbirth=0):
        with conn:
            cur = conn.cursor()
            cursor = cur.execute("INSERT INTO artist(name ,dateofbirth ) VALUES (?,?) ", (name ,dateofbirth))
        print("artist added successfully")
        print('######################################################')
    def delete_artist(self,name):
        f=True
        with conn:
            cur = conn.cursor()
            find=cur.execute("SELECT  dateofbirth, COUNT(*) FROM artist   where name = ?", (name,))
            for row in find:
                if row[0] != None:
                   f=False
                   break;
        if f == True:   
            print("this name not found in data base")
        else:
            with conn:
              cur = conn.cursor()
              cursor = cur.execute("SELECT name from song where featuredartist = ?",(name,))
              for row in cursor:
                  n=str(row[0])
                  cur.execute("UPDATE song SET featuredartist = 'NULL'  where name = ?", (n,))
              cur.execute("DELETE FROM artist   where name = ?", (name,))
              print("artist delete successfully")
        print('######################################################')
                  
        
########## end of class artist ###########

#########  class album ###############
class Album:
        def __init__(self,title=0,bandname=0,numberofsongs=0 ):
            if title!=0:
                self.title=title 
                self.bandname=bandname 
                self.numberofsongs=numberofsongs
        def view_all_albums(self):
            with conn:
                cur = conn.cursor()
                cursor = cur.execute("SELECT name,numberofsongs from  album")
            for row in cursor:
                print(row[0]," Tracks : ",row[1])
            print('######################################################')    
        def add_album(self,name,band,numberofsongs):
            f=True
            with conn:
                cur = conn.cursor()
                find=cur.execute("SELECT  name FROM album   where name = ?", (name,))
                for row in find:
                    if row[0] != None:
                        f=False
                        break
            if f== True:
                with conn:
                    cur = conn.cursor()
                    cursor = conn.execute("INSERT INTO album(name ,bandname,numberofsongs ) VALUES (?,?,?) ", (name ,band,numberofsongs))
                    print("album added successfully")
            else:
                print("this album is already in database")
            print('######################################################')
            
        def view_album(self,name):
            with conn:
                cur = conn.cursor()
                cursor = conn.execute("SELECT name,length from  song  WHERE albumname=? ",(name,))
            for row in cursor:
                print(row[0]," Duration : ",row[1])
                
            print('######################################################')
            
        def delete_album(self,name):
            f=True
            with conn:
                cur = conn.cursor()
                find=cur.execute("SELECT bandname FROM album  where name = ?", (name,))
                for row in find:
                    if row[0] != None:
                       f=False
                       break
            if f == True:   
                print("this name not found in data base")
            else:
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM album   where name = ?", (name,))
                    print("album delete successfully")
            print('######################################################')
        
########## end of class album ###########
            
######### song class ###############
class Song:
    def __init__(self,name=0,band=0,featuredartist=0,album=0,releasedate=0,genres=0,lyrics=0,length=0,place=0): 
        if name!=0 :   
            self.name=name #string
            self.band=band #object from band 
            self.featuredartist=featuredartist # string
            self.album=album #object from album
            self.releasedate=releasedate #string
            self.genres=genres #string 
            self.lyrics=lyrics #string
            self.length=length #double
            self.place=place
            
    def viwe_all_songs(self):
        cursor = conn.execute("SELECT name,length from  song")
        for row in cursor:
            print(row[0]," Duration : ",row[1])
        print('######################################################')
        
    def view_song(self,name):
        cursor = conn.execute("SELECT * from  song WHERE name=? ",(name,))
        for row in cursor:
            print("Song: ",name)
            print("Band/Artist: ",row[1])
            print("Featured artist/band: ",row[2])
            print("Album: ",row[3])
            print("Release date: ",row[4])
            print("Genres: ",row[5])
            print("lyrics: ",row[6])
            print("Duration :",row[7])
        print('######################################################')
    
    def add_song(self,songname,lyics,length,bandname,artistname,albumname,genere,release,place):
        find = conn.execute("SELECT name from song WHERE name=? ",(songname,))
        f=True
        for row in find:
            if row[0] != None:
                f=False
                break
        if f==False:
            print("already exist song")
            return 0
        else:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO song(name ,bandName,featuredartist,albumname,releasedate,genres,lyrics,length,place ) VALUES (?,?,?,?,?,?,?,?,?) ", (songname ,bandname,artistname,albumname,release,genere,lyics,length,place))
                print("song added successfuly")
    def song_with_certain_band(self,bandname):
        cursor = conn.execute("SELECT name,length from song WHERE bandname=? ",(bandname,))
        for row in cursor:
            print(row[0]," Duration: ",row[1])
        print('######################################################')
        
    def song_with_certain_genre(self,genrename):
        cursor = conn.execute("SELECT name,length from song WHERE genres=? ",(genrename,))
        for row in cursor:
            print(row[0]," Duration: ",row[1])
        print('######################################################')
        
    def song_with_certain_artist(self,artistname):
        cursor = conn.execute("SELECT name,length from song WHERE featuredartist=? ",(artistname,))
        for row in cursor:
            print(row[0]," Duration: ",row[1])
        newcursor = conn.execute("SELECT bandname from artistwithband WHERE artistname=? ",(artistname,))
        for row in cursor:
            bandname=row[0]
            newcursor = conn.execute("SELECT name,length from song WHERE bandname=? ",(bandname,))
            for record in newcursor:
                print(record[0]," Duration: ",record[1])   
        print('######################################################')
    
    def delete_song(self,nameofsongs):
         f=True
         with conn:
                cur = conn.cursor()
                find=cur.execute("SELECT   name FROM song   where name = ?", (nameofsongs,))
                for row in find:
                    if row[0] != None:
                       f=False
                       break
                if f==True:
                     print("undefine song")
                     return 0
         with conn:
                 cur = conn.cursor()
                 playlists=cur.execute("SELECT playlistname FROM songswithplaylists WHERE songname=?",(nameofsongs,))
                 listnamesplaylist=[]
                 listnamesalbums=[]
                 for r in playlists:
                     n=str(r[0])
                     listnamesplaylist.append(n)

                 cur.execute("DELETE  FROM song WHERE name=?",(nameofsongs,))
                 cur.execute("DELETE  FROM songswithplaylists WHERE songname=?",(nameofsongs,))
                 for i in listnamesalbums:
                     cur.execute("UPDATE album  SET numberofsongs = numberofsongs-1  where name = ?", (i,))
                 for i in listnamesplaylist:
                     cur.execute("UPDATE playlist SET numebersons = numebersons-1 where name = ?", (i,))
         print('######################################################')
            
        
########## end of class song ###########
        
######### playlist class ###############
class Playlist:
    def __init__(self,name=0,listofsongs=0,description=0):   
        if name!=0:
            self.name = name #string 
            self.description = description #string 
            self.numsongs= numsongs #object from songs
    def viw_all_playlist(self):
        cursor = conn.execute("SELECT name,numebersons from playlist")
        for row in cursor:
            print(row[0]," Trak:",row[1])
        print('######################################################')
    def sort_one_playlist(self,name,method,order):
        print(name)
        d = conn.execute("SELECT description FROM  playlist where name = ?",(name,))
        for row in d:
            print(row[0])
        if method == 'a': #sort by name
            songsIn = conn.execute("SELECT songname FROM  songswithplaylists where playlistname = ? ORDER BY songname", (name,))
            songsInPlaylist = []
            for row in songsIn:
                songsInPlaylist.append(str(row[0]))
            if order == 1:
                for row in songsInPlaylist:
                    song = conn.execute("SELECT name,length from song WHERE name=? ",(row,))
                    for item in song:
                        print(item[0]," Duration: ",item[1])
            elif order == 2:
                for row in reversed(songsInPlaylist):
                    song = conn.execute("SELECT name,length from song WHERE name=? ",(row,))
                    for item in song:
                        print(item[0]," Duration: ",item[1])
        elif method == 'b':#sort by artist
            find = conn.execute("SELECT name,length ,albumname  FROM  songswithplaylists  INNER JOIN song  ON songname = name where playlistname =  ? ORDER BY featuredartist", (name,))
            clean = []
            for row in find:
                clean.append(row)
            if order==1:
                for row in clean:
                    print("name ",row[0],"length",row[1],"artist " ,row[2])
            if order==2:
                rev=[]
                i=(len(clean))
                while True:
                    i=i-1
                    if i<0:
                        break
                    rev.append(clean[i])
                for row in rev:
                    print("name ",row[0],"length",row[1],"featuredartist " ,row[2])
        elif method == 'c':#album
            find = conn.execute("SELECT name,length ,albumname  FROM  songswithplaylists  INNER JOIN song  ON songname = name where playlistname = ? ORDER BY albumname", (name,))
            clean = []
            for row in find:
                clean.append(row)
            if order==1:
                for row in clean:
                    print("name ",row[0],"length",row[1],"album " ,row[2])
            if order==2:
                rev=[]
                i=(len(clean))
                while True:
                    i=i-1
                    if i<0:
                        break
                    rev.append(clean[i])
                for row in rev:
                    print("name ",row[0],"length",row[1],"album " ,row[2])
                    
        elif method == 'd':#genre
            find = conn.execute("SELECT name,length ,genres  FROM  songswithplaylists  INNER JOIN song  ON songname = name where playlistname = ? ORDER BY genres", (name,))
            clean = []
            for row in find:
                clean.append(row)
            if order==1:
                for row in clean:
                    print("name ",row[0],"length",row[1],"genres " ,row[2])
            if order==2:
                rev=[]
                i=(len(clean))
                while True:
                    i=i-1
                    if i<0:
                        break
                    rev.append(clean[i])
                for row in rev:
                    print("name ",row[0],"length",row[1],"genres " ,row[2])
        
        elif method == 'e':#release date
            find = conn.execute("SELECT name,length ,releasedate  FROM  songswithplaylists  INNER JOIN song  ON songname = name where playlistname = ? ORDER BY releasedate", (name,))
            clean = []
            for row in find:
                clean.append(row)
            if order==1:
                for row in clean:
                    print("name ",row[0],"length",row[1],"releasedate " ,row[2])
            if order==2:
                rev=[]
                i=(len(clean))
                while True:
                    i=i-1
                    if i<0:
                        break
                    rev.append(clean[i])
                for row in rev:
                    print("name ",row[0],"length",row[1],"releasedate " ,row[2])
        
        print('######################################################')
        
    def add_playlist(self,name,description=0):
        f=True
        with conn:
            cur = conn.cursor()
            find=cur.execute("SELECT name  FROM playlist   where name = ?", (name,))
            for row in find:
                print(row[0])
                if row[0] != None:
                   f=False
                   break
        if f == True:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO playlist(name,description,numebersons) VALUES (?,?,?) ",(name,description,0))
                print("playlist added succesfuly")
        else :
            print("this playlist in database")
        print('######################################################')
        
    def add_song_to_playlist(self,nameofplaylist,nameofsong):
        cur = conn.cursor()
        find=cur.execute("SELECT name FROM song   where name = ?", (nameofsong,))
        f=True
        for row in find:
            if row[0] != None:
               f=False
               break
        if f == True: 
            print("undefine song")
        else:
             f=True
             with conn:
                 cur = conn.cursor()
                 find=cur.execute("SELECT name  FROM playlist   where name = ?", (nameofplaylist,))
             for row in find:   
                 if row[0] != None:
                    f=False
                    break
             if f == True:   
                     print("undefine playlist")
             else:                
                 f=True
                 cur = conn.cursor()
                 find=cur.execute("SELECT songname  FROM  songswithplaylists  where playlistname = ?", (nameofplaylist,))
                 for row in find:
                     if row[0] == nameofsong:
                        f=False
                        break
                 if f == False :       
                     print("this song is alerady in playlist")
                 else:
                    with conn:
                        cur = conn.cursor()
                        cur.execute("INSERT INTO songswithplaylists(songname,playlistname) VALUES (?,?) ",(nameofsong,nameofplaylist ))
                        cur.execute("UPDATE  playlist SET numebersons = numebersons+1  where name = ?", (nameofplaylist,))
                        print("song is added successfuly")
        print('######################################################')
        
    def delete_playlist(self,name):
        f=True
        find = conn.execute("SELECT description  FROM playlist   where name = ?", (name,))
        for row in find:
            if row[0] != None:
                f=False
                break
        if f==True:
            print("undifine laylist")
        else:
            with conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM songswithplaylists   where playlistname = ?", (name,))
                cur.execute("DELETE FROM  playlist  where name = ?", (name,))
                print("playlist deleted succesfuly")
        print('######################################################')
    
    def reomve_song_paly_list(self,nameofplaylist,nameofsong):
        f=True
        with conn:
            cur = conn.cursor()
            find=cur.execute("SELECT name FROM song   where name = ?", (nameofsong,))
        for row in find:
            if row[0] != None:
               f=False
               break
        if f == True:   
          print("undefine song")
        else:
             f=True
             with conn:
                    cur = conn.cursor()
                    find=cur.execute("SELECT description  FROM playlist   where name = ?", (nameofplaylist,))
                    for row in find:
                        if row[0] != None:
                           f=False
                           break
             if f == True:   
                     print("undefine playlist")
             else:
                 f=True
                 with conn:
                    cur = conn.cursor()
                    find=cur.execute("SELECT songname  FROM  songswithplaylists  where playlistname = ?", (nameofplaylist,))
                    for row in find:
                        if row[0] == nameofsong:
                           f=False
                           break
                 if f == False :
                     with conn:
                        cur = conn.cursor()
                        cur.execute("DELETE FROM songswithplaylists  where songname = ? AND playlistname =? ",(nameofsong,nameofplaylist,))
                        cur.execute("UPDATE  playlist SET numebersons = numebersons-1  where name = ?", (nameofplaylist,))
                 else:
                     print("this songis not in playlist")

        print('######################################################')  
        
        
########### main ##################
while True :
    print("Welcome To Musicly")
    print("0. exist 1. Playlists 2. Artists 3. Albums 4. Library")
    choice = input()
    if(choice == "0" ):
        break 
    elif(choice == '1' ):#playlist
        print("Welcome To Musicly")
        print("<< Playlists >>")
        playlist = Playlist()
        playlist.viw_all_playlist()
        print("1. View playlist")
        print("2. Back to Home")
        print("3. Add playlist")
        print("4. Delete playlist")
        print("5. add song to playlist")
        print("6. remove song from playlist") 
        choice = input()
        if( choice == '1'):
            name = input("enter the name of playlist")
            print("sort by a. name     b. artist   c. album   d. genre   e. release date .")
            method=input("enter method")
            print("orderofascending 1 /  orderofdecinging 2 ")
            a=input("enter")
            s=int(a)
            playlist.sort_one_playlist(name,method ,s)
        elif(choice == '2'):
            print('######################################################')
            continue
        elif( choice == '3'):
            name = input("enter the name of playlist")
            description = input("enter description")
            playlist.add_playlist(name,description)           
        elif( choice == '4'):
            name = input("enter the name of playlist")
            playlist.delete_playlist(name)
        elif(choice == '5'):
            print("a. new song    b.exist song")
            enter = input("enter you choice")
            if enter =='a':
               songname = input("enter the name of song")
               lyics = input("enter the lyrics of song")
               length = input("enter the length")
               bandname = input("enter the bandname")
               artistname = input("enter the artistname")
               albumname = input("enter the albumname")
               genere = input("enter the genere")
               release =input("enter the release date")
               place =input("enter the place of song")
               song = Song()
               song.add_song(songname,lyics,length,bandname,artistname,albumname,genere,release,place)
            elif enter == 'b':
               songname = input("enter the name of song")
                      
            name = input("enter the name of playlist")
            playlist.add_song_to_playlist(name,songname)
        elif(choice == '6'):
            name = input("enter the name of playlist")
            song = input("enter the name of song")
            playlist.reomve_song_paly_list(name,song)
            
    elif(choice == '2'):#artist
        print("Welcome To Musicly")
        print("<< Artists >>")
        artist = Artist()
        artist.view_all()
        print("1. Play all songs to certain artist ")
        print("2. Back to Home")
        print("3. Add Artist")
        print("4. Delete Artist")
        choice = input()
        if(choice == '1'):
           name = input("enter the name of artist")
           artist.view_artist(name)
        if(choice == '2'):
            print('######################################################')
            continue
        if(choice == '3'):
            name = input("enter the name of artist")
            dateofbirth = input("enter the date of birth of artist")
            artist.add_artist(str(name),str(dateofbirth))
        if(choice == '4'):
            name=input("enter the name of artist")
            artist.delete_artist(str(name))
    elif(choice == '3'):#album
        print("Welcome To Musicly")
        print("<< Albums >>")
        album = Album()
        album.view_all_albums()
        print("1. View Album")
        print("2. Back to Home")
        print("3. Add Album")
        print("4. Delete Album")
        choice = input()
        if(choice == '1'):
           name = input("enter the name of Album")
           album.view_album(name)
        if(choice == '2'):
            print('######################################################')
            continue
        if(choice == '3'):
            name = input("enter the name of Album")
            bandname = input("enter the Band/Artist name of Album")
            numberofsongs = input("enter the number of songs")
            album.add_album(str(name),str(bandname),int(numberofsongs))
        if(choice == '4'):
            name=input("enter the name of Album")
            album.delete_album(str(name))
            
    elif(choice=='4'):#songs
        print("Welcome To Musicly")
        print("<< Songs >>")
        song = Song()
        song.viwe_all_songs()
        print("1. View song")
        print("2. Back to Home")
        print("3. Play all songs to certain genre. ")
        print("4. Play all songs to certain band")
        print("5. Play all songs to certain artist")
        print("6. Delete song")
        choice = input()
        if(choice=='1'):
            name = input("enter the name of song")
            song.view_song(name)
        elif(choice=='2'):
            print('######################################################')
            continue
        elif(choice=='3'):
            genrename = input("enter the name of genre")
            song.song_with_certain_genre(genrename)
        elif(choice=='4'):
            bandname = input("enter the name of band")
            song.song_with_certain_band(bandname)
        elif(choice=='5'):
            artistname = input("enter the name of artist")
            song.song_with_certain_artist(artistname)
        elif(choice=='6'):
            name = input("enter the name of song")
            song.delete_song(name)           
       
conn.close()        
        