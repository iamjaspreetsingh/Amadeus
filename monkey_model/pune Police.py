import pyrebase
import cv2
import winsound
i=1

config = {
  "apiKey": "apiKey",
  "authDomain": "bageera2018.firebaseapp.com",
  "databaseURL": "https://bageera2018.firebaseio.com",
  "storageBucket": "bageera2018.appspot.com",
  #"serviceAccount": "path/to/serviceAccountCredentials.json"
}
config2 = {
  "apiKey": "apiKey",
  "authDomain": "lifesaver-18f28.firebaseapp.com",
  "databaseURL": "https://lifesaver-18f28.firebaseio.com",
  "storageBucket": "lifesaver-18f28.appspot.com",
  #"serviceAccount": "path/to/serviceAccountCredentials.json"
}
def stream_handler(message):
    global i
    if i != 1:
        #print(message)
        #users = db.child("users").get()
        #print(users.val())
        users=message["data"]
        print(users)
        dlink=str(users)
        print(dlink)
        storage.child(dlink).download("downloaded.jpeg")
        #print(img)
        #mat = cv2.imread('downloaded.jpeg',0)
        #print(mat)
        #cv2.imshow('downloaded.jpeg',mat)
        a=cv2.imread('downloaded.jpeg')
        #print(a)
        #sound = pyttsx.init()
        #sound.say('Emergency')
        #sound.runAndWait()
        
        cv2.imshow('check',a)
        winsound.PlaySound('siren.wav', winsound.SND_FILENAME)
        cv2.waitKey(0)
        print('Should the people be notified about the incident?')
        ups=input()
        if ups == 'y':
            name2,gps = dlink.split('-')
            #name1,name=name2.split('\'')
            gps2,jpg=gps.split('.')
            print(name2)
            print(gps2)
            val={'Description':"Women in emergency",'GPS':gps2,'Prob':'Emergency'}
            print(val)
            update.child("PROBLEMS").child(name2).set(val)
            update.update({'notify': '1'})
    else:
        i=2

firebase = pyrebase.initialize_app(config)
fb=pyrebase.initialize_app(config2)
storage = firebase.storage()
update=fb.database()

#storage.child("example.jpeg").put("thumbDiv.jpeg")
#db.child("users").set({1:"example.jpeg"})

db = firebase.database()
my_stream = db.child("users").stream(stream_handler)

#users = db.child("users").get()
#dlink=users.val()
#print(dlink[1])
#storage.child(dlink[1]).download("downloaded.jpg")

