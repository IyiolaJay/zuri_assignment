class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
        self.name = str(name)
        print("Name is ", name,"and student's age is", self.age,"The student track is", self.tracks, "Score: ",self.score)

    def add_track(self, track):
        tracks= ['FE', 'BE']
        tracks.insert(2, track)
        print(tracks)
    
    def change_age(self, age):
        self.age = int(age)

    def get_score(self):
        print(self.score)
        

age_new = 40
track = input('Enter Preferred track: \n')
newname = input("Enter your name here: \n")
Bob = Student(name = 'Bob', age=age_new, tracks=track, score=20.90)
Bob.change_name(newname)
Bob.change_age(age_new)
Bob.add_track(track)
Bob.get_score()