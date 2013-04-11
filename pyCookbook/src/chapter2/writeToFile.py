'''
Created on 2013-4-10

@author: buaa
'''
all_the_text=''
all_the_data=''
list_of_text_Strings=''
sequence_of_strings=''
open('thefile.txt','w').write(all_the_text)
open('thefile.txt','wb').write(all_the_data)
file_object = open('thefile.txt', 'w')
file_object.write(all_the_text)
file_object.close( )
#字符串列表中(对文本和二进制都生效)
file_object.write(list_of_text_Strings)
open('abinfile','wb').writelines(sequence_of_strings)      #use write need join first
#ab  r+b