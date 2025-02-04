def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    # number_of_students = 0

    # for scores in student_scores:
    #     if scores > 40:
    #         number_of_students += 1

    # return number_of_students
    return sum([1 for score in student_scores if score <= 40])

# print(count_failed_students([40, 40, 35, 70, 30, 41, 90]))


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    interval = (highest-40)//4

    # return [41, 41+interval, 41+interval*2, 41+interval*3]

    score = []

    for grade in range(0,4):
        score.append(41 + interval*grade)

    return score

# print(letter_grades(100))

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    students_rank = [f'{rank}. {student}' for rank, student in enumerate(student_names)]

    # students_rank_score = [ for score in student_scores]

    # for student, score in zip(students_rank, student_scores):
    #     print(student, score)

    # for (rank, student), score in zip(enumerate(student_names), student_scores):
    #     print(f'{rank}. {student}: {score}')

    students_rank = [f'{rank+1}. {student}: {score}' for (rank, student), score in zip(enumerate(student_names), student_scores)]

    return students_rank


student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']

# print(student_ranking(student_scores, student_names))s

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        # print(student[1])
        if student[1] != 100:
            continue
        if student[1] == 100:
            return student
        
    return []

# print(perfect_score([['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],              ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]]))

print(perfect_score( [['Jill', 30], ['Paul', 73]]))