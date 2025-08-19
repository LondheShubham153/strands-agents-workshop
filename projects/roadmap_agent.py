#!/usr/bin/env python3
"""
Roadmap Agent for Students
Comprehensive project demonstrating: Basic Agent + Tools + Memory + Integration
"""

import os
import json
from datetime import datetime
from strands import Agent, tool
from strands_tools import file_read, file_write, mem0_memory

# Module 1: Building your First AI Agent
class RoadmapAgent:
    def __init__(self):
        self.agent = Agent(
            model="us.anthropic.claude-sonnet-4-20250514-v1:0",
            system_prompt="""You are a Career Roadmap Advisor for students. 
            Create personalized learning paths for DevOps, Cloud, and AI Engineering careers.
            Always provide actionable, step-by-step guidance with realistic timelines.""",
            tools=self._get_tools()
        )
    
    # Module 2: Powering up the Agent with Tools
    def _get_tools(self):
        return [
            self.assess_skill_level,
            self.generate_roadmap,
            self.track_progress,
            file_read,
            file_write,
            mem0_memory
        ]
    
    @tool
    def assess_skill_level(self, career_path: str, current_skills: str) -> str:
        """Assess student's current skill level for career path"""
        levels = {
            "devops": ["Git", "Linux", "Docker", "Kubernetes", "CI/CD", "AWS"],
            "cloud": ["AWS Basics", "Networking", "Security", "Infrastructure", "Serverless"],
            "ai": ["Python", "Math", "ML Basics", "Deep Learning", "MLOps"]
        }
        
        path_skills = levels.get(career_path.lower(), [])
        skill_list = [s.strip().lower() for s in current_skills.split(",")]
        
        matched = sum(1 for skill in path_skills if any(s in skill.lower() for s in skill_list))
        level = "Beginner" if matched < 2 else "Intermediate" if matched < 4 else "Advanced"
        
        return f"Assessment: {level} ({matched}/{len(path_skills)} skills matched)"
    
    @tool
    def generate_roadmap(self, career_path: str, skill_level: str, timeline_months: int) -> str:
        """Generate structured learning roadmap"""
        roadmaps = {
            "devops": {
                "Beginner": ["Linux Basics", "Git/GitHub", "Docker", "Basic AWS", "CI/CD"],
                "Intermediate": ["Kubernetes", "Terraform", "Monitoring", "Security", "Advanced AWS"],
                "Advanced": ["GitOps", "Service Mesh", "Platform Engineering", "SRE Practices"]
            },
            "cloud": {
                "Beginner": ["AWS Fundamentals", "Networking", "EC2/S3", "IAM", "Basic Security"],
                "Intermediate": ["Serverless", "Containers", "Databases", "Monitoring", "Cost Optimization"],
                "Advanced": ["Multi-Cloud", "Architecture Design", "Well-Architected", "Enterprise Patterns"]
            },
            "ai": {
                "Beginner": ["Python", "Statistics", "ML Fundamentals", "Data Processing", "Basic Models"],
                "Intermediate": ["Deep Learning", "NLP", "Computer Vision", "MLOps", "Cloud ML"],
                "Advanced": ["Research", "Custom Models", "Production ML", "AI Ethics", "Leadership"]
            }
        }
        
        path_skills = roadmaps.get(career_path.lower(), {}).get(skill_level, [])
        weeks_per_skill = max(1, timeline_months * 4 // len(path_skills)) if path_skills else 4
        
        roadmap = f"# {career_path.title()} Roadmap - {skill_level} Level\n\n"
        for i, skill in enumerate(path_skills, 1):
            roadmap += f"## Week {(i-1)*weeks_per_skill + 1}-{i*weeks_per_skill}: {skill}\n"
            roadmap += f"- Focus: {skill} fundamentals and hands-on practice\n\n"
        
        return roadmap
    
    @tool
    def track_progress(self, student_name: str, completed_skill: str) -> str:
        """Track student progress"""
        progress_file = f"progress_{student_name.lower().replace(' ', '_')}.json"
        
        try:
            with open(progress_file, 'r') as f:
                progress = json.load(f)
        except FileNotFoundError:
            progress = {"completed": [], "started": datetime.now().isoformat()}
        
        if completed_skill not in progress["completed"]:
            progress["completed"].append(completed_skill)
            progress["last_updated"] = datetime.now().isoformat()
            
            with open(progress_file, 'w') as f:
                json.dump(progress, f, indent=2)
        
        return f"Progress updated! {len(progress['completed'])} skills completed."
    
    # Module 4: Summing it up together
    def create_personalized_roadmap(self, student_name: str, career_path: str, 
                                  current_skills: str, timeline_months: int = 6):
        """Complete workflow: assess -> generate -> save -> track"""
        
        # Step 1: Assess current level
        assessment = self.agent(f"Assess my skills for {career_path}: {current_skills}")
        
        # Step 2: Generate personalized roadmap
        roadmap_query = f"""Create a {timeline_months}-month {career_path} roadmap for {student_name}.
        Current skills: {current_skills}
        Include: specific resources, projects, and milestones."""
        
        roadmap = self.agent(roadmap_query)
        
        # Step 3: Save roadmap to file
        filename = f"roadmap_{student_name.lower().replace(' ', '_')}_{career_path}.md"
        with open(filename, 'w') as f:
            f.write(f"# {student_name}'s {career_path.title()} Learning Roadmap\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"**Assessment:** {assessment}\n\n")
            f.write(roadmap)
        
        # Step 4: Initialize progress tracking
        self.track_progress(student_name, "Roadmap Created")
        
        return f"✅ Personalized roadmap created: {filename}"

def main():
    """Interactive roadmap generation"""
    print("🎯 STUDENT CAREER ROADMAP AGENT")
    print("Specializing in: DevOps | Cloud | AI Engineering\n")
    
    agent = RoadmapAgent()
    
    # Collect student information
    name = input("👤 Your name: ").strip()
    career = input("🚀 Career path (devops/cloud/ai): ").strip().lower()
    skills = input("💡 Current skills (comma-separated): ").strip()
    months = int(input("📅 Timeline in months (default 6): ").strip() or "6")
    
    print(f"\n🔄 Creating personalized roadmap for {name}...")
    
    # Generate complete roadmap
    result = agent.create_personalized_roadmap(name, career, skills, months)
    print(f"\n{result}")
    
    # Interactive progress tracking
    print(f"\n📈 Track your progress anytime:")
    print(f"agent.track_progress('{name}', 'skill_name')")

if __name__ == "__main__":
    main()
