
from utilites import *

user_input = "Reduce physical oracle refresh timeline by leveraging delphix"

system_prompt1 = "WHW stands for What How Why framework of asking questions. Rewrite the below sentence in WHW framework\n" + user_input
system_prompt2 = "How is it achieved currently ? Produce from knowledge and user to validate."
system_prompt3 = "How is it achieved currently ? Generate related questionnaire for user to provide more context"
system_prompt4 = "Gather knowledge on the technique"
system_prompt5 = "Generate and suggest quantitative KPIs and validated by user"

print(system_prompt1)
##llmresponse1 = useLLM(system_prompt1)
##llmresponse2 = useLLM(system_prompt2)
##llmresponse3 = useLLM(system_prompt3)
##llmresponse4 = useLLM(system_prompt4)
##llmresponse5 = useLLM(system_prompt5)