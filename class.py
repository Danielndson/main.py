class Student:
    # [assignment] Skeleton class. Add your code here
      def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

      def change_name(self, name):
        self.name=name
        
            
      def change_age(self, age):
        self.age =int(age)
        

      def change_track(self, string):
        self.track.append(string)

        

      def get_score(self):
            return self.score




Bob = Student("Bob", 26,["FE","BE"],20.90)

