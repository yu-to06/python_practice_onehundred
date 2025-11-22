class Student:
    def __init__(self, name, math, japanese, english, science, society):
        self.name = name
        self.math = int(math)
        self.japanese = int(japanese)
        self.english = int(english)
        self.science = int(science)
        self.society = int(society)

    # 平均点を計算するメソッド
    def average_score(self):
        avg = (
            self.math + self.japanese + self.english + self.science + self.society
        ) / 5
        return avg


student_saitou = Student("斉藤", 85, 90, 78, 88, 92)
avg_score = student_saitou.average_score()
print(f"{student_saitou.name}さんの5教科の平均点は{avg_score}です")
