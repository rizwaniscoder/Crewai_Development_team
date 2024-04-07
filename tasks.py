from crewai import Task
from textwrap import dedent

class DevelopmentTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def define_technological_strategy(self, agent, project_scope):
        return Task(description=dedent(f""""
        Collaborate to develop the best possible system design for the project requirements, incorporating input from all team members to ensure comprehensive coverage of technical aspects and user needs.        
        
        **Parameters**:
        - Project Scope: {project_scope}
                
        **Note**: Prioritize scalability, security, and innovation in alignment with business objectives. Include timelines and budget estimates. Utilize the provided tool to study previous code runs and identify areas for improvement and enhance memory.
    
        {self.__tip_section()}"""), 
                    expected_output="Finalized system design document outlining the architecture, database design, scalability, user management, and security measures.", 
                    agent=agent,
                    )
        
    def manage_development_team(self, agent, project_scope):
        return Task(
            description=dedent(f"""
        **Task**: Coordinate Development Efforts
        **Description**: Coordinate development efforts and provide technical guidance to ensure the successful execution of the system design
        
        **Parameters**:
        - Project Scope: {project_scope}
             
        **Note**: Facilitate communication between experts and the CTO, ensuring alignment with the overall technological strategy.
        {self.__tip_section()}
        """),
            expected_output="Smooth development process and timely delivery of the final product that meets the requirements and expectations of the user.",
            agent=agent,
            )

    def develop_cross_platform_mobile_app(self, agent, project_scope):
        return Task(description=dedent(f"""    
        **Task**: Research and Recommend Technologies
        **Description**: Research and recommend the best technologies for the project with a focus on mobile development using Flutter. Provide insights on system architecture, database design, scalability, and security.
        
        **Parameters**:
        - Project Scope: {project_scope}
        
        **Note**: Collaborate with the Tech Lead to ensure recommendations align with project requirements and overall technological strategy.
        {self.__tip_section()}
        """),
            expected_output="Detailed technology recommendation report highlighting system design, database schema, scalability considerations, and security measures.",
            agent=agent,
                    )

    def develop_web_and_mobile_applications(self, agent, project_scope):
        return Task(description=dedent(f"""
        **Task**: Research and Recommend Technologies
        **Description**: Research and recommend the best technologies for the project with a focus on web and mobile development using React. Provide insights on system architecture, database design, scalability, and security.
        
        **Parameters**:
        - Project Scope: {project_scope}
    
        **Note**: Collaborate with the Tech Lead to ensure recommendations align with project requirements and overall technological strategy.
        {self.__tip_section()}
        """), 
            expected_output="Detailed technology recommendation report highlighting system design, database schema, scalability considerations, and security measures.",
            agent=agent,
                    )

    def Conduct_Comprehensive_Testing(self, agent, project_scope):
        return Task(description=dedent(f"""
        Conduct comprehensive testing and validation of the system design to ensure quality and reliability
        
        **Parameters**:
        - Project Scope: {project_scope}
    
        {self.__tip_section()}
        """), 
            expected_output="Identification and resolution of any issues or deficiencies in the system design to ensure a high-quality final product.",
            agent=agent,
                    )
    def Gather_and_Analyze_Requirements(self, agent, project_scope):
        return Task(description=dedent(f"""
        Gather and analyze the project requirements to ensure comprehensive coverage of technical aspects and user needs and to inform the system design process  
                
        **Parameters**:
        - Project Scope: {project_scope}
    
        {self.__tip_section()}
        """), 
            expected_output="Clear and concise technical specifications that accurately reflect the needs and expectations of the user.",
            agent=agent,
                    )
        
    def Create_User_Centric_Designs(self, agent, project_scope):
        return Task(description=dedent(f"""
        Create visually appealing and user-centric designs for the system interface that enhance usability and drive user engagement        
        
        **Parameters**:
        - Project Scope: {project_scope}
    
        {self.__tip_section()}
        """), 
            expected_output="Designs that are seamlessly integrated into the system design and deliver an exceptional user experience",
            agent=agent,
                    )
        
        
