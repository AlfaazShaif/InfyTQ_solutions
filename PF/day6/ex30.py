#PF-Exer-30

def find_average(mark_list):
    total=0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except TypeError:
        print("Wrong Data Type")
    except NameError:
        print("Name Error")

try:
    mark1 = "A"
    mark1 = int('A')
    m_list = [mark1,2,3,4]
    print("Average Marks: ", find_average(m_list))
except NameError:
    print("Name Error")
except TypeError:
    print("Type Error")
except ValueError:
    print("Value Error")