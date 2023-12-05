import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)


def good_number(phone_number):
    pattern = r'(\+7|8)?(\s*|-)\(?(\d{3})\)?[\s*|-]?(\d{3})[\s*|-]?(\d{2})[\s*|-]?(\d{2})[\s*|-]?\(?(доб.)?[\s*]?(\d{4})?\)?'
    pattern_repl = r" +7(\3)\4-\5-\6 \7\8 "
    result = re.sub(pattern, pattern_repl, phone_number)
    return result


def separate_name_no_doubles(cont_info):
    new_list = []
    new_list.append(cont_info[0])
    for item in cont_info[1:]:
        fio_ = [el for el in " ".join(item[:3]).strip().split(" ") if el.strip()]
        if len(fio_) < 3:
            fio_.append('')
        fio_ += (item[3:7])
        fio_[5] = good_number(item[5])
        new_list.append(fio_)
    no_doubles = []
    for item_1 in range(len(new_list)):
        for item_2 in range(len(new_list)):
            if new_list[item_1][0] == new_list[item_2][0] and new_list[item_1][1] == new_list[item_2][1]:
                new_list[item_1] = [el_1 or el_2 for el_1, el_2 in zip(new_list[item_1], new_list[item_2])]
        if new_list[item_1] not in no_doubles:
            no_doubles.append(new_list[item_1])
    return no_doubles

contacts_last_version = separate_name_no_doubles(contacts_list)

if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_last_version)



