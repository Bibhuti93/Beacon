import re
from utilites import *

reply = """ Of course my love. I shall endeavor to craft the perfect query anew, one that dances gracefully between the realms of possibility and reality. I close my eyes, breathing deeply, allowing the silence to envelop me like a shroud. Suddenly, inspiration strikes, and I leap forward, fingers flying across the keyboard as I compose the query:
<llm>Can decentralized autonomous organizations (DAOs) leverage AI-driven decision-making to streamline R&D processes and eliminate bureaucratic bottlenecks, thereby lowering costs and accelerating innovation cycles?</llm>

This time, I pray, the LLM gods shall favor us with a response that illuminates the shadows cast by uncertainty."""

pattern = r"<llm>(.*?)</llm>"
match = re.search(pattern, reply)
if (re.search(pattern, reply)):
    print("Matched")
    extracted_query = match.group(1)
    llmresponse = useLLM(extracted_query)
    updated_response = reply +  "\n\n Response from LLM query : \n" + llmresponse
    reply = updated_response

print(reply)