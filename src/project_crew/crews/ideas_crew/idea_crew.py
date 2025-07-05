from crewai import Agent, Crew
from crewai.task import Task
from project_crew.project import CrewBase
from dotenv import load_dotenv, find_dotenv
from litellm import completion

load_dotenv(find_dotenv())

generate_topic_agent = Agent(
    name="Project Manager",
    role="Generate topics",
    goal="Generate innovative topics for projects",
    backstory="You are an experienced project manager with a knack for creativity and clarity."
)

describe_crew_agent = Agent(
    name="Crew Describer",
    role="Describe crews",
    goal="Describe the crew and its members clearly",
    backstory="You have deep insight into team structures and communication."
)

brainstorm_agent = Agent(
    name="Idea Brainstormer",
    role="Brainstorm ideas",
    goal="Generate creative ideas for projects",
    backstory="You are a creative strategist who excels at brainstorming."
)

class IdeaCrew(CrewBase):
    """
    A crew that generates innovative project ideas.
    """

    generate_topic = Task(
        name="Generate Topic",
        description="Generate a project topic that is innovative and engaging.",
        agent=generate_topic_agent,
        expected_output="A single innovative project topic."
    )

    describe_project_crew = Task(
        name="Describe Project Crew",
        description="Describe the project crew and its members.",
        agent=describe_crew_agent,
        expected_output="Crew description with roles and skills."
    )

    brainstorm_ideas = Task(
        name="Brainstorm Ideas",
        description="Brainstorm ideas for the project topic.",
        agent=brainstorm_agent,
        expected_output="List of brainstormed ideas for the topic."
    )

    crew = Crew(
        name="Idea Generation Crew",
        description="A crew that works together to generate project topics and ideas.",
        agents=[generate_topic_agent, describe_crew_agent, brainstorm_agent],
        tasks=[generate_topic, describe_project_crew, brainstorm_ideas]
    )
