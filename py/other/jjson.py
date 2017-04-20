def student2dict(a):
    return {
        'nnnaaa': a.name,
        'age': a.age,
        'score': a.score
    }

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# >>> from jjson import Student, student2dict
# >>> s = Student('haha', 22, 100)
# >>> import json
# >>> json.dumps(s, default=student2dict)
# '{"age": 22, "nnnaaa": "haha", "score": 100}'
