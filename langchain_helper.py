from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate # Components
from langchain.chains import LLMChain # Chains
from langchain.agents import initialize_agent # all three are for agents
from langchain.agents import load_tools
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_colour):
    llm = OpenAI(temperature=0.7) # more creative as it nears 1
    prompt_template = PromptTemplate(
        input_variables=['animal_type', 'pet_colour'],
        template="I have a {animal_type}, its {pet_colour} in colour and i want to name it with a cool name, suggest five cool names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key='pet_name') # what kind of repsonse you want bascilly the subject

    response = name_chain({'animal_type': animal_type,
                           'pet_colour': pet_colour}) # passing params to prompt

    return response # json response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(['wikipedia', 'llm-math'], llm=llm) # tools for the agent to work with

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    ) # agent type initialized

    response = agent.run(
        'What is the average age of a dog?, Divide it by 3'
    ) # response from agent

    print(response)

if __name__ == '__main__':
    langchain_agent()
