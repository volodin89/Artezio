class Student:

    def __init__(self, name: str, conf):
        self.name = name
        self.conf = conf
        self.progress = {}

    def make_lab(self, m, n=1):
        if n > 0:
            self.progress.update({n: m})

    def make_exam(self, m):
        if 0 < m <= self.conf.get("exam_max"):
            self.progress.update({"exam": m})

    def total_point(self):
        total_lab_point = 0
        for i in range(1, self.conf.get("lab_num") + 1):
            if 0 < self.progress.get(i) <= self.conf.get("lab_max"):
                total_lab_point += self.progress.get(i)
        total_point = self.progress.get("exam") + total_lab_point
        return total_point

    def is_certified(self):
        total_point = self.total_point()
        max_point = self.conf.get("exam_max") + self.conf.get("lab_max") * self.conf.get("lab_num")
        if total_point / max_point > self.conf.get("k"):
            return total_point, True
        return total_point, False
