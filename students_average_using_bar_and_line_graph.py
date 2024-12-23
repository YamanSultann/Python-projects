import matplotlib.pyplot as plt

students_names = ["Sova","James","Violet","Lameya","Akshay","Saad","Xhuanghu"]
students_marks = [48,35,43,22,50,40,50]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(students_names,marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Percentage")
    plt.show()

percentage_bar_chart()