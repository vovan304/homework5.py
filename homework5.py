immutable_var_ = 1, 'u', 3, False
print(type(immutable_var_))
print(immutable_var_)
#immutable_var_[3] =True ошибка, кортеж - неизменяемый тип данных
mutable_list = [3, 4, 'f','G', 'late']
print(mutable_list)
mutable_list[0] = 10
mutable_list[1] = 18
mutable_list[-3] = 't'
mutable_list[-2] = 'W'
mutable_list[-1] = 'early'
print(mutable_list)