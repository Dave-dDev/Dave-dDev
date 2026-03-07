class PersonalizedTutoringEngine:
    def __init__(self):
        self.students = {}
        self.difficulties = ["beginner", "intermediate", "advanced", "expert"]

    def add_student(self, student_id, name):
        """Adds a new student to the tutoring engine."""
        if student_id not in self.students:
            self.students[student_id] = {
                "name": name,
                "difficulty_index": 0,
                "consecutive_high_scores": 0,
                "consecutive_low_scores": 0,
                "history": []
            }
            print(f"Student {name} (ID: {student_id}) added at difficulty {self.difficulties[0]}.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def get_lesson(self, student_id):
        """Returns the current lesson difficulty for the student."""
        if student_id in self.students:
            student = self.students[student_id]
            difficulty = self.difficulties[student["difficulty_index"]]
            print(f"Lesson for {student['name']}: Difficulty level - {difficulty}")
            return difficulty
        else:
            print("Student not found.")
            return None

    def record_score(self, student_id, score):
        """Records a score and adjusts difficulty based on performance."""
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]
        student["history"].append(score)
        print(f"Recorded score {score} for {student['name']}.")

        if score >= 85:
            student["consecutive_high_scores"] += 1
            student["consecutive_low_scores"] = 0
            if student["consecutive_high_scores"] >= 2:
                self._increase_difficulty(student_id)
        elif score <= 50:
            student["consecutive_low_scores"] += 1
            student["consecutive_high_scores"] = 0
            if student["consecutive_low_scores"] >= 2:
                self._decrease_difficulty(student_id)
        else:
            student["consecutive_high_scores"] = 0
            student["consecutive_low_scores"] = 0

    def _increase_difficulty(self, student_id):
        student = self.students[student_id]
        if student["difficulty_index"] < len(self.difficulties) - 1:
            student["difficulty_index"] += 1
            student["consecutive_high_scores"] = 0
            print(f"Difficulty increased! {student['name']} is now at {self.difficulties[student['difficulty_index']]} level.")
        else:
            print(f"{student['name']} is already at the maximum difficulty level ({self.difficulties[-1]}).")

    def _decrease_difficulty(self, student_id):
        student = self.students[student_id]
        if student["difficulty_index"] > 0:
            student["difficulty_index"] -= 1
            student["consecutive_low_scores"] = 0
            print(f"Difficulty decreased. {student['name']} is now at {self.difficulties[student['difficulty_index']]} level.")
        else:
            print(f"{student['name']} is already at the minimum difficulty level ({self.difficulties[0]}).")

if __name__ == "__main__":
    engine = PersonalizedTutoringEngine()

    # Add a student
    engine.add_student("S001", "Alice")

    # Get a lesson
    engine.get_lesson("S001")

    # Record scores to increase difficulty
    engine.record_score("S001", 90)
    engine.record_score("S001", 88)
    engine.get_lesson("S001")

    # Record scores to increase difficulty again
    engine.record_score("S001", 95)
    engine.record_score("S001", 100)
    engine.get_lesson("S001")

    # Record mediocre score, difficulty should remain the same
    engine.record_score("S001", 70)
    engine.get_lesson("S001")

    # Record scores to decrease difficulty
    engine.record_score("S001", 45)
    engine.record_score("S001", 30)
    engine.get_lesson("S001")

    # Record score for non-existent student
    engine.record_score("S002", 80)
