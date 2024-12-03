import datetime,os

#Формирование матрицы из файла начальных данных
def get_matrix_input(input_data):
        matrix_data = []
        for string in input_data:
            raw_data = string.replace('\n', '').replace('-', ',').split(',')
            matrix_data.append(raw_data)
        if not matrix_data[0][0].isdigit():
            del matrix_data[0]
        return matrix_data

#Формирования списка посещений по дням недели
def get_list_count_people_weekday(list):
    weekday_data = [['Monday', 0],
                    ['Tuesday', 0],
                    ['Wednesday', 0],
                    ['Thursday', 0],
                    ['Friday', 0],
                    ['Saturday', 0],
                    ['Sunday', 0]]

    for elem in list:
        day = datetime.datetime(int(elem[0]), int(elem[1]), int(elem[2])).weekday()
        weekday_data[day][1] += int(elem[-1])
    return weekday_data

#Формирование списка посещений по месяцам
def get_list_count_people_month(matrix):
    sum_month = 0
    month = matrix[0][1]
    year = matrix[0][0]
    output = []
    for elem in matrix:
            if month == elem[1]:
                sum_month += int(elem[-1])
            else:
                output.append([year+' '+month,sum_month])
                month = elem[1]
                sum_month = int(elem[-1])
    output.append([year+' '+month,sum_month])
    return output

#сортировка по убыванию
def sort_up(list):
    for i in range(1,len(list),1):
        elem = list[i]
        j = i - 1
        while (j >= 0 and elem[-1] > list[j][-1]):
                list[j+1] = list[j]
                j=j-1
        list[j+1] = elem
    return list

#сортировка по возрастанию
def sort_down(list):
    for i in range(1,len(list),1):
        elem = list[i]
        j = i - 1
        while (j >= 0 and elem[-1] < list[j][-1]):
                list[j+1] = list[j]
                j=j-1
        list[j+1] = elem
    return list

#Вывод результатов в лог файл
def output_results(month_data,sort_weekday_up,sort_day_down):
    output_data = open('mod_5_task_5_output.txt', 'w')
    output_data.write('The most popular months:\n')
    for elem in month_data:
        output_data.write(f'Month: {elem[0]}, Count visitors: {elem[-1]} people\n')

    output_data.write('\nThe most popular days of the week:\n')
    for elem in sort_weekday_up:
        output_data.write(f'Weekday: {elem[0]}, Count visitors: {elem[-1]} people\n')

    output_data.write('\nThe days with the least attendance:\n')
    for elem in sort_day_down:
        weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.datetime(int(elem[0]), int(elem[1]), int(elem[2])).weekday()
        output_data.write(f'Day: {elem[0]}.{elem[1]}.{elem[2]} ({weekday[day]}), Count visitors: {elem[-1]} people\n')
    output_data.close()

def check_error_isfile(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f'Файл {path} не найден')

    file = open(path, 'r+')
    if os.stat(path).st_size != 0 and (file.readline() != '' or file.readline() != '\n'):
        file.close()
        return path
    else:
         raise ValueError(f'Файл {path} пуст')

def check_matrix_empty(matrix):
    if matrix == [] or matrix[0][0] == '' or len(matrix[0])<4:
        raise ValueError(f'В файле нет значений для обработки')


def main(path_file):
    check_error_isfile(path_file)
    input_data = open(path_file, 'r')

    matrix_data = get_matrix_input(input_data)
    check_matrix_empty(matrix_data)

    weekday_data = get_list_count_people_weekday(matrix_data)
    month_data = get_list_count_people_month(matrix_data)
    sort_weekday_up = sort_up(weekday_data)
    sort_day_down = sort_down(matrix_data)

    input_data.close()
    output_results(month_data,sort_weekday_up,sort_day_down)










