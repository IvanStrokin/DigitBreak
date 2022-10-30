import statistics
import reformat_data


def get_param(data_elem):
    max_data = []
    min_data = []
    i = 0
    while i < len(data_elem):
        flag_max = False
        count = 0
        while i + 1 < len(data_elem) and data_elem[i] < data_elem[i + 1]:
            count += 1
            flag_max = True
            i += 1
        if count < 4:
            flag_max = False

        if flag_max:
            max_data.append(i)
        flag_min = False
        count = 0
        while i + 1 < len(data_elem) and data_elem[i] > data_elem[i + 1]:
            count += 1
            flag_min = True
            i += 1

        if count < 4:
            flag_min = False

        if flag_min:
            min_data.append(i)
        if not (flag_max or flag_min):
            i += 1

    new_count = 4
    while len(min_data) < 8 or len(max_data) < 5:
        max_data = []
        min_data = []
        new_count -= 1
        i = 0
        while i < len(data_elem):
            flag_max = False
            count = 0
            while i + 1 < len(data_elem) and data_elem[i] < data_elem[i + 1]:
                count += 1
                flag_max = True
                i += 1
            if count < new_count:
                flag_max = False

            if flag_max:
                max_data.append(i)
            flag_min = False
            count = 0
            while i + 1 < len(data_elem) and data_elem[i] > data_elem[i + 1]:
                count += 1
                flag_min = True
                i += 1

            if count < new_count:
                flag_min = False

            if flag_min:
                min_data.append(i)
            if not (flag_max or flag_min):
                i += 1

    if len(max_data) > len(min_data):
        max_data = max_data[:len(min_data)]
    else:
        min_data = min_data[:len(max_data)]

    ampl_list = []
    if max_data[0] > min_data[0]:
        for i in range(len(min_data) - 1):
            diff_1 = data_elem[max_data[i]] - data_elem[min_data[i]]
            diff_2 = data_elem[min_data[i + 1]] - data_elem[max_data[i]]
            ampl_list.append(abs(diff_1))
            ampl_list.append(abs(diff_2))
    else:
        for i in range(len(min_data) - 1):
            diff_1 = data_elem[min_data[i]] - data_elem[max_data[i]]
            diff_2 = data_elem[max_data[i + 1]] - data_elem[min_data[i]]
            ampl_list.append(abs(diff_1))
            ampl_list.append(abs(diff_2))

    avg_ampl = sum(ampl_list) / len(ampl_list)
    ampl_diff = [round(abs(avg_ampl - ampl) / avg_ampl * 100, 0) for ampl in ampl_list]
    ampl_result = sum(ampl_diff) / len(ampl_diff)

    frick_list = [max_data[i + 1] - max_data[i] for i in range(len(max_data) - 1)]
    max_frick = max(frick_list)
    min_frick = min(frick_list)
    mode_frick = statistics.mode(frick_list)
    max_frick_per = abs(max_frick - mode_frick) / mode_frick * 100
    min_frick_per = abs(mode_frick - min_frick) / mode_frick * 100
    frick_result = (min_frick_per + max_frick_per) / 2
    i = 0
    offset_list = []
    while i < len(max_data):
        flag_max = False
        first_i = i
        count = 0
        while i + 1 < len(max_data) and data_elem[max_data[i]] < data_elem[max_data[i + 1]]:
            flag_max = True
            i += 1
        if flag_max:
            diff = data_elem[max_data[first_i]] - data_elem[max_data[i]]
            offset_list.append(abs(diff))
        flag_min = False
        while i + 1 < len(max_data) and data_elem[max_data[i]] > data_elem[max_data[i + 1]]:
            diff = data_elem[max_data[first_i]] - data_elem[max_data[i]]
            offset_list.append(abs(diff))
            flag_min = True
            i += 1
        if not (flag_max and flag_min):
            i += 1
    if offset_list == []:
        return [frick_result, ampl_result, 0.0]
    offset_avg = sum(offset_list) / len(offset_list)
    if offset_avg == 0:
        return [frick_result, ampl_result, 0.0]
    offset_per_list = [abs(offset_avg - offset) / offset_avg * 100 for offset in offset_list]
    offset_result = sum(offset_per_list) / len(offset_per_list)
    return [frick_result, ampl_result, offset_result]
