from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv
from litellm import completion
from project_crew.crews.ideas_crew.idea_crew import IdeaCrew

# Load environment variables from .env file
load_dotenv(find_dotenv())

class Project(Flow):
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": """Create a project topic that is
                    innovative and engaging, suitable for a team of diverse skills."""
                }
            ],
            max_tokens=100,
            temperature=0.5,
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 topic: {self.state['topic']}")

    @listen("generate_topic")
    def brainstorm_ideas(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": f"""Brainstorm ideas for the project topic: {self.state['topic']}"""
                }
            ],
            max_tokens=200,
            temperature=0.7,
        )
        self.state['ideas'] = response['choices'][0]['message']['content']
        print(f"STEP 2 ideas: {self.state['ideas']}")

    @listen("brainstorm_ideas")
    def describe_project_crew(self):
        # Initialize IdeaCrew
        idea_crew = IdeaCrew()

        # Kick off the crew execution
        idea_crew.crew.kickoff()

        crew_description = "This crew is composed of diverse members with unique skills."
        print(f"STEP 3 crew description: {crew_description}")
        self.state['crew_description'] = crew_description

def kickoff():
    flow = Project()
    flow.kickoff()
