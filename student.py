class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)

    def update_branch(self, new_branch):
        self.branch = new_branch

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "branch": self.branch
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["branch"]
        )