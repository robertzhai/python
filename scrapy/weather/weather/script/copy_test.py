# -*- coding: utf-8 -*-
import copy
dict ={"a":"apple","o":"orange"}
dict2 ={"b":"banana","p":"pear"}
#copy.deepcopy等价于dict.deepcopy
dict2 = copy.deepcopy(dict)
#copy.copy 等价于dict.copy
dict3 = copy.copy(dict)
dict2["a"]="watermelon"
dict3["a"]="juice"

print dict,dict2,dict3