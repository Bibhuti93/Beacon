
from utilites import *

user_input = "Reduce physical oracle refresh timeline by leveraging delphix"

prompt1 = "WHW stands for What How Why framework of asking questions. Rewrite the below sentence in WHW framework \n Generate in below format \n **What:** \n **How:** \n **Why:**" + user_input
llmresponse1 = useLLM(prompt1)
print(llmresponse1)
print("+ ---------------------------------------------- +")

what = "Extract text from below statement for What \n The text starts after **What:** \n" + llmresponse1
how = "Extract text from below statement of How \n The text starts after **How:** \n" + llmresponse1
why = "Extract text from below statement of Why \n The text starts after **Why:** \n" + llmresponse1
whatresponse = useLLM(what)
howresponse = useLLM(how)
whyresponse = useLLM(why)

print(whatresponse)
print(howresponse)
print(whyresponse)

print("+ ---------------------------------------------- +")

prompt3 = whatresponse + "Extract the task from the above statement and answer the following. How is achieved currently ? Produce from knowledge and ask user to validate."
llmresponse3 = useLLM(prompt3)
print(llmresponse3)

print("+ ---------------------------------------------- +")

prompt4 = "How is " + whatresponse + " achieved currently ? Generate related questionnaire for user to provide more context"
prompt5 = "Gather knowledge on the technique mentioned in : " + howresponse
prompt6 = "Generate and suggest quantitative KPIs and validated by user"

