class Dog:
    def __init__(self, name):
        self.name=name
        self.cls='dog'
    def setCount(self,val):
        self.count=val
    def getCount(self):
        return self.count
class Cat:
    def __init__(self, name):
        self.name=name
        self.cls='cat'
    def setCount(self, val):
        self.count=val
    def getCount(self):
        return self.count
class PetEnter:
    def __init__(self):
        self.DogQ=[]
        self.CatQ=[]
        self.count=0
    def add(self, pet):
        if pet.cls=='dog':
            self.DogQ.append(pet)
            self.count +=1
            pet.setCount(self.count)
        elif pet.cls=='cat':
            
            self.CatQ.append(pet)
            self.count +=1
            pet.setCount(self.count)
        else:
            raise Exception('It must be a dog or cat!')

    def pollAll(self):
        if not self.is_catEmpty() and not self.is_dogEmpty():
            if self.DogQ[0].getCount() < self.CatQ[0].getCount():
                polldog=self.DogQ.pop(0)
                return polldog.name, polldog.getCount()
            else:
                pollcat=self.CatQ.pop(0)
                return pollcat.name, pollcat.getCount()
        elif self.is_catEmpty():
            polldog=self.DogQ.pop(0)
            return polldog.name, polldog.getCount()
        elif self.is_dogEmpty():
            pollcat=self.CatQ.pop(0)
            return pollcat.name, polcat.getCount()
        else:
            raise Exception('Both queues are empty!')
    def pollDog(self):
        if self.is_dogEmpty():
            raise Exception('dog queue is empty')
        a=self.DogQ.pop(0)
        return a.name, a.getCount
    def is_empty(self):
        return not self.DogQ and not self.CatQ
    def is_dogEmpty(self):
        return not self.DogQ
    def is_catEmpty(self):
        return not self.CatQ
    def show(self):
        if not self.is_dogEmpty():
            print('Dog queue:')
            for i in self.DogQ:
                print(i.name, i.getCount(), end=' ')
            print(' ')
        if not self.is_catEmpty():
            print('Cat queue:')
            for i in self.CatQ:
                print(i.name, i.getCount(), end=' ')
            print(' ')
if __name__=='__main__':
    dog1=Dog("dog1")
    cat1=Cat("cat1")
    dog2=Dog("dog2")
    cat2=Cat("cat2")
    dog3=Dog("dog3")
    cat3=Cat("cat3")
    queue=PetEnter()
    queue.add(dog1)
    queue.add(cat1)
    queue.add(dog2)
    queue.add(cat2)
    queue.add(dog3)
    queue.add(cat3)

    print("now queue:")
    queue.show()
    a=queue.pollAll()
    print(a)
    b=queue.pollAll()
    print(b)
    
            
            


