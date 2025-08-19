# 🚀 Strands Agents Workshop Projects

Practical projects demonstrating core Strands Agents concepts through real-world applications.

## 📁 Projects Overview

### 1. 🎯 Student Career Roadmap Agent
**File:** `roadmap_agent.py`

A comprehensive agent that creates personalized learning roadmaps for students pursuing DevOps, Cloud, and AI Engineering careers.

**Features:**
- Skill level assessment
- Personalized roadmap generation
- Progress tracking with JSON persistence
- Memory-enabled conversations
- Markdown roadmap output

**Modules Demonstrated:**
- ✅ Basic Agent Creation
- ✅ Tool Integration (assessment, generation, tracking)
- ✅ Memory Support (mem0_memory)
- ✅ File Operations (roadmap saving)

**Usage:**
```bash
python roadmap_agent.py
# Follow interactive prompts for name, career path, skills, timeline
```

### 2. 🌟 Motivational Chat Assistant
**File:** `motivational_assistant.py`

A lightweight, witty chat assistant that provides motivation and inspiration through live API integration.

**Features:**
- Witty, encouraging conversations
- Live motivational quotes from API
- Daily motivation boosts
- Simple interactive chat

**Modules Demonstrated:**
- ✅ Basic Agent Creation
- ✅ API Integration (http_request tool)
- ✅ Custom Tools (motivation, quotes)
- ✅ Error Handling (API fallbacks)

**Usage:**
```bash
python motivational_assistant.py
# Chat naturally, type 'quote' or 'motivation' for specific content
```

## 🎓 Learning Path

### For Beginners
Start with **Motivational Assistant** - simple, lightweight, immediate results

### For Advanced Users
Try **Roadmap Agent** - comprehensive workflow, file operations, memory

## 🔧 Requirements

- Python 3.8+
- AWS Bedrock access (Claude Sonnet 4)
- Virtual environment activated
- Optional: MEM0_API_KEY for memory features

## 🚀 Quick Start

```bash
# From workshop root
source venv/bin/activate
cd projects

# Run simple demo
python motivational_assistant.py

# Run comprehensive project
python roadmap_agent.py
```

## 📊 Project Comparison

| Feature | Motivational Assistant | Roadmap Agent |
|---------|----------------------|---------------|
| **Complexity** | Simple (~80 lines) | Comprehensive (~150 lines) |
| **Token Usage** | Low | Moderate |
| **Demo Time** | 2-3 minutes | 5-10 minutes |
| **Use Case** | Quick demos, inspiration | Learning workflows, persistence |
| **Tools** | API, motivation | Assessment, generation, tracking |
| **Output** | Chat responses | Markdown files, JSON progress |

## 🎯 Perfect For

- **Live Demos** - Both projects work great for presentations
- **Learning** - Progressive complexity from simple to advanced
- **Workshops** - Interactive, engaging examples
- **Development** - Real-world patterns and best practices

## 📚 Additional Files

- `example_output.md` - Sample roadmap output
- `motivational_README.md` - Detailed assistant documentation

---

**Choose your adventure: Start simple with motivation, or dive deep with roadmaps!** 🌟
