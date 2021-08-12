import pyrebase



def downloadSong(song,type):
    config = {"apiKey": "AIzaSyBpaO7Km0omfiANZKT2WNuwQPfu2D3_2Es",
  "authDomain": "robotappmusic.firebaseapp.com",
  "databaseURL": "https://robotappmusic-default-rtdb.firebaseio.com",
  "projectId": "robotappmusic",
  "storageBucket": "robotappmusic.appspot.com",
  "messagingSenderId": "723665809146",
  "appId": "1:723665809146:web:7ae7bba454eb8c8ba6a343",
  "measurementId": "G-T38D8SJXT3"};
    firebase = pyrebase.initialize_app(config)
    storeage = firebase.storage()
    path =  "/song"+type+"/song" + str(song)
    storeage.child(path).download('song'+type+str(song)+'.mp3','song'+type+str(song)+'.mp3')
    print("finished")
if __name__ == "__main__":
    downloadSong(1,"Flying")
    downloadSong(2,"Dancing")
#     downloadSong(1,"KeyMsg")