# Strands Agents Workshop

A comprehensive workshop for building AI agents with the Strands framework on AWS Cloud. This workshop provides both Jupyter notebook and Python script formats for flexible delivery.

## 🎯 Workshop Overview

This 2-3 hour workshop takes participants from basic agent creation to advanced multi-agent systems, covering:

- Basic agent creation and configuration
- Tool integration and custom capabilities
- Multi-model support (AWS Bedrock + Ollama)
- Memory-enabled agents with persistence
- Advanced real-world applications
- Multi-agent system orchestration
- MCP (Model Context Protocol) integration

## 📁 Repository Structure

```
strands-agents-workshop/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── SETUP.md                 # Detailed setup instructions
├── CONTRIBUTING.md          # Contribution guidelines
├── notebooks/               # Jupyter notebook format
│   ├── 01-basic-agent-creation.ipynb
│   ├── 02-working-with-tools.ipynb
│   ├── 03-custom-models.ipynb
│   ├── 04-memory-enabled-agents.ipynb
│   ├── 05-advanced-examples.ipynb
│   ├── 06-multi-agent-systems.ipynb
│   ├── 07-mcp-integration.ipynb
│   └── README.md
├── scripts/                 # Python script format
│   ├── 01_basic_agents.py
│   ├── 02_agent_tools.py
│   ├── 03_custom_models.py
│   ├── 04_memory_agents.py
│   ├── 05_advanced_examples.py
│   ├── 06_multi_agent_systems.py
│   ├── 07_mcp_integration.py
│   ├── mcp.json
│   └── README.md
├── .env.example            # Environment variables template
└── venv/                   # Virtual environment
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- AWS Account with Bedrock access
- (Optional) Ollama for local models

### Setup
```bash
# Clone and navigate
cd strands-agents-workshop

# Create virtual environment (if not exists)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your AWS credentials and API keys

# Alternative: Configure AWS (choose one method)
aws configure  # Interactive setup
# OR
export AWS_PROFILE=your-profile
export AWS_REGION=us-west-2
```

### Choose Your Format

#### Option 1: Jupyter Notebooks (Recommended for Interactive Learning)
```bash
jupyter notebook notebooks/
```

#### Option 2: Python Scripts (IDE Development)
```bash
cd scripts
python 01_basic_agents.py
```

## 🎓 Learning Path

### Module 1: Foundation (30 minutes)
- **01-basic-agent-creation**: Create your first agents
- **02-working-with-tools**: Add capabilities with tools

### Module 2: Models & Memory (45 minutes)
- **03-custom-models**: AWS Bedrock and Ollama integration
- **04-memory-enabled-agents**: Persistent conversations

### Module 3: Advanced Applications (60 minutes)
- **05-advanced-examples**: Real-world use cases
- **06-multi-agent-systems**: Agent orchestration

### Module 4: Integration (30 minutes)
- **07-mcp-integration**: Model Context Protocol

### Configuration

Copy the example environment file and configure your settings:
```bash
cp .env.example .env
# Edit .env with your AWS credentials and preferences
```

### AWS Bedrock Setup
```bash
# Ensure your AWS credentials have Bedrock access
aws bedrock list-foundation-models --region us-west-2
```

### Ollama Setup (Optional)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull recommended models
ollama pull llama3.2:1b
ollama pull llama3.2:3b
```

### Memory Configuration (Optional)
```bash
# For Mem0 integration
export MEM0_API_KEY=your-api-key
```

## 📚 Documentation

- [Official Strands Agents Docs](https://strandsagents.com/latest/documentation/docs/) - Official documentation
- [Setup Instructions](SETUP.md) - Detailed environment setup
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- [API Reference](docs/API_REFERENCE.md) - Strands Agents API guide
- [Contributing](CONTRIBUTING.md) - How to contribute

## 🆘 Support

For issues and questions:
1. Check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
2. Review notebook comments and documentation
3. Verify your environment setup

## 📄 License

This workshop content is provided for educational purposes.

---

**Ready to build intelligent agents? Start with `notebooks/01-basic-agent-creation.ipynb` or `scripts/01_basic_agents.py`!**
