import pandas as pd

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]


# def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
#     # dictionary of lists
#     # dict = {'student_id': student_data, 'age': student_data}
#     df = pd.DataFrame(student_data, columns=('student_id', 'age'))
#     return df


df = pd.DataFrame(student_data, columns=('student_id', 'age'))

def toKnowLen(df) -> list:
    return df[df.student_id == 3].drop('student_id', axis=1)


print(toKnowLen(df))
