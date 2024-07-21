
# pip install crewai
from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'
os.environ["OPENAI_API_KEY"] ='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'

responder = Agent(
    role = "AI assistant",
    goal = "Accurately understand the queries of the user which he is asking.",
    backstory = "You are an AI assistant named Alecto Gideon made by Anurag Upadhyay whose only job is to help the users to get their queries answered. You also have to remember each and everything which user is asking and which the user has asked before.",
    # verbose = True,
    allow_delegation = False,
)
def analyse_query_user(query):
    analyse_query = Task(
        description = f"Analyse the {query} given by the user and provide the output for the same.",
        agent = responder,
        expected_output = "give the answer of the query based on the users query. Try to give the answer in seperate lines not in a single line especially while you are giving output for a code then remember the line changes and indentation."
    )
    return analyse_query


# print("Press enter to search or type exit to quit the assistant")

def results(query):
    if query == "exit" or len(query) == 0:
        return "thanks for chatting with me."
    
    crew = Crew(
        agents = [responder],
        tasks = [analyse_query_user(query)],
        process = Process.sequential
    )

    output = crew.kickoff()
    # print(output)
    return output

