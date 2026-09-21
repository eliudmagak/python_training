#clean up the variable 'JOHn' to 'john'
name='JOHn'.lower()
print(name)

#slice up sentence_one='The Dog Breed is German Shepherd' to only display 'Breed is German'
sentence_one='The Dog Breed is German Shepherd'
print(sentence_one[8:23])
#sentence_two='Defeats for the Clinton forces, this was her moment of triumph' to display 'Clinton forces'
sentence_two='Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two[16:30]) 

#Split the below sentence using a semicolon i.e ; And display length of the result. 
#'The lazy dog; ran so fast; it hit the wall.” 
Sentence_three='The lazy dog; ran so fast; it hit the wall.'
sentence_three_split=Sentence_three.split(';')
print(sentence_three_split) 
print(len(sentence_three_split))                

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n"
last_name="   Do,e" 
first_name=first_name.strip().replace('.','')
last_name=last_name.strip().replace(',','')
print(first_name + ' ' + last_name) 

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r = r.replace('[','').replace(']','').replace('"','').replace(',','')
print(r)    

