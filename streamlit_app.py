import streamlit as st
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import DevelopmentAgents
from tasks import DevelopmentTasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DevelopmentCrew:
    def __init__(self, project_scope):
        self.project_scope = project_scope

    def run(self):
        agents = DevelopmentAgents()
        tasks = DevelopmentTasks() 

        chief_tech_officer = agents.chief_tech_officer()
        tech_lead = agents.tech_lead()
        flutter_dev = agents.flutter_dev()
        react_dev = agents.react_dev()
        business_analyst = agents.business_analyst()
        tester = agents.tester()
        designer = agents.designer()

        define_technological_strategy = tasks.define_technological_strategy(
            chief_tech_officer,
            self.project_scope,
        )

        manage_development_team = tasks.manage_development_team(
            tech_lead,
            self.project_scope,
        )
        
        develop_cross_platform_mobile_app = tasks.develop_cross_platform_mobile_app(
            flutter_dev,
            self.project_scope,
        )
        
        develop_web_and_mobile_applications = tasks.develop_web_and_mobile_applications(
            react_dev,
            self.project_scope,
        )
        
        Conduct_Comprehensive_Testing = tasks.Conduct_Comprehensive_Testing(
            tester,
            self.project_scope,
        )
        
        Gather_and_Analyze_Requirements = tasks.Gather_and_Analyze_Requirements(
            business_analyst,
            self.project_scope,
        )
        
        Create_User_Centric_Designs = tasks.Create_User_Centric_Designs(
            designer,
            self.project_scope,
        )

        crew = Crew(
            agents=[tech_lead, flutter_dev, react_dev, business_analyst, tester, designer, chief_tech_officer],
            tasks=[manage_development_team, develop_cross_platform_mobile_app, develop_web_and_mobile_applications, Conduct_Comprehensive_Testing, Gather_and_Analyze_Requirements, Create_User_Centric_Designs, define_technological_strategy],
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125"),
            verbose=True,
        )

        result = crew.kickoff()
        return result

def main():
    st.title("Technical Crew AI")
    st.markdown("---")

    project_scope = st.text_area("Project Scope")

    if st.button("Run Development Crew"):
        custom_crew = DevelopmentCrew(project_scope)
        result = custom_crew.run()
        st.write("## Development Crew Run Result:")
        st.write(result)

        with open("Previous_results.txt", "a") as file:
            file.write("\n\n########################\n")
            file.write("## Previous Development Crew Run Result:\n")
            file.write("########################\n")
            file.write(result)

if __name__ == "__main__":
    main()

