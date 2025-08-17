# Strands Agents Workshop

A comprehensive, hands-on workshop for building AI agents with the Strands framework. This workshop takes you from basic concepts to production-ready multi-agent systems.

## Workshop Overview

This workshop provides a structured learning path through 6 progressive notebooks, each building on the previous concepts while introducing new capabilities.

### [01-basic-agent-creation.ipynb](./01-basic-agent-creation.ipynb)
**Foundation: Your First Agent**
- Creating agents with default and custom configurations
- Understanding system prompts and agent personalities
- Model configuration and best practices
- Error handling and debugging techniques

**What you'll build:**
- Basic conversational agents
- Specialized role-based agents (technical expert, business analyst)
- Task-specific agents (code reviewer, summarizer)

### [02-working-with-tools.ipynb](./02-working-with-tools.ipynb)
**Extending Capabilities: Tools and Actions**
- Creating custom tools with the `@tool` decorator
- Using built-in tools from `strands-agents-tools`
- Error handling and input validation
- Combining multiple tools for complex workflows

**What you'll build:**
- Mathematical calculation tools
- File operation tools
- Web API integration tools
- Data analysis tools

### [03-custom-models.ipynb](./03-custom-models.ipynb)
**Model Selection: Cloud and Local Options**
- Amazon Bedrock model configurations
- Local model deployment with Ollama
- Performance comparison and optimization
- Cost-effective model selection strategies

**What you'll learn:**
- When to use Claude Sonnet vs Haiku
- Setting up local models for privacy
- Model fallback mechanisms
- Performance monitoring

### [04-memory-enabled-agents.ipynb](./04-memory-enabled-agents.ipynb)
**Persistent Memory: Stateful Conversations**
- Mem0 integration for persistent memory
- User preference storage and retrieval
- Contextual conversation handling
- Memory management best practices

**What you'll build:**
- Agents that remember user preferences
- Personalized recommendation systems
- Context-aware conversation agents

### [05-advanced-examples.ipynb](./05-advanced-examples.ipynb)
**Real-World Applications**
- Personal finance assistant
- Research and note-taking agent
- Task management system
- Multi-agent orchestration patterns

**What you'll build:**
- Production-ready applications
- Complex workflow systems
- Data persistence patterns

### [06-multi-agent-systems.ipynb](./06-multi-agent-systems.ipynb)
**Advanced Orchestration: Teams of Agents**
- Swarm-based agent coordination
- Graph-based agent workflows
- Parallel processing patterns
- Agent communication protocols

**What you'll build:**
- Coordinated agent teams
- Structured multi-agent workflows
- Complex task decomposition systems

### [07-mcp-integration.ipynb](./07-mcp-integration.ipynb)
**MCP Integration: External System Connectivity**
- Model Context Protocol (MCP) fundamentals
- Connecting to MCP servers from Strands Agents
- AWS Diagram MCP server integration
- Multi-server MCP configurations

**What you'll build:**
- MCP-enabled agents with external capabilities
- AWS architecture visualization agents
- Multi-system integration patterns
- Robust error handling for external connections

## Quick Start

### Prerequisites
- Python 3.8 or higher
- AWS credentials configured (for default Bedrock provider)
- Basic Python and Jupyter knowledge

### Installation Options

#### Option 1: Automated Setup (Recommended)
```bash
cd notebooks
python setup.py
jupyter notebook
```

#### Option 2: Manual Setup
```bash
cd notebooks
pip install -r requirements.txt
jupyter notebook
```

#### Option 3: Quick Start
```bash
cd notebooks
pip install strands-agents strands-agents-tools jupyter
jupyter notebook 01-basic-agent-creation.ipynb
```

## Learning Paths

### Beginner Path (2-3 hours)
1. **01-basic-agent-creation.ipynb** - Core concepts (45 min)
2. **02-working-with-tools.ipynb** - Adding capabilities (60 min)
3. **03-custom-models.ipynb** - Model selection (30 min)

### Intermediate Path (4-5 hours)
1. Complete beginner path
2. **04-memory-enabled-agents.ipynb** - Persistent memory (90 min)
3. **05-advanced-examples.ipynb** - Real applications (90 min)

### Advanced Path (6-8 hours)
1. Complete all notebooks in sequence
2. **06-multi-agent-systems.ipynb** - Complex orchestration (120 min)
3. **07-mcp-integration.ipynb** - External system integration (60 min)
4. Build custom applications using learned concepts

### Expert Path (8-10 hours)
1. Complete all 7 notebooks
2. Implement production-ready applications
3. Integrate multiple MCP servers
4. Build comprehensive multi-agent systems with external capabilities

## Configuration

### Model Configuration
The workshop uses consistent model configuration across all notebooks:

```python
# Primary models
DEFAULT_MODEL = "anthropic.claude-sonnet-4-20250514-v1:0"
BEDROCK_CLAUDE_HAIKU = "anthropic.claude-3-5-haiku-20241022-v1:0"
OLLAMA_LLAMA = "llama3.2:1b"  # For local deployment
AWS_REGION = "us-west-2"
```

### AWS Setup
For Amazon Bedrock (default provider):
```bash
# Configure AWS credentials
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-west-2
```

### Optional: Local Models
For privacy or offline usage:
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama3.2:1b

# Start Ollama service
ollama serve
```

### Optional: Memory Features
For persistent memory examples using [Mem0](https://mem0.ai/):
```bash
# Get API key from mem0.ai (free tier available)
export MEM0_API_KEY=your-mem0-api-key
```

## Workshop Features

### Production-Ready Code
- Comprehensive error handling
- Input validation and sanitization
- Security best practices
- Performance optimization techniques

### Real-World Examples
- Practical applications you can deploy
- Industry-standard patterns
- Scalable architectures

### Progressive Learning
- Each notebook builds on previous concepts
- Clear explanations and code comments
- Practice exercises and challenges

### Quality Assurance
- All notebooks tested and verified
- Consistent coding standards
- Professional documentation

## Troubleshooting

### Common Issues

**Import Errors**
```bash
pip install --upgrade strands-agents strands-agents-tools
```

**AWS Authentication**
- Verify AWS credentials: `aws sts get-caller-identity`
- Check Bedrock model access in AWS console
- Ensure correct region configuration

**Jupyter Issues**
```bash
pip install --upgrade jupyter notebook ipykernel
jupyter notebook --generate-config
```

**Memory Examples Not Working**
```bash
pip install mem0ai opensearch-py
# Check API key configuration
```

### Getting Help
1. Check notebook comments and documentation
2. Review error messages carefully
3. Try simpler examples first
4. Verify environment configuration

## Advanced Topics

### Production Deployment
- Docker containerization
- Kubernetes orchestration
- Monitoring and logging
- Security hardening

### Performance Optimization
- Model selection strategies
- Caching mechanisms
- Parallel processing
- Resource management

### Integration Patterns
- Database connectivity
- API gateway integration
- Message queue systems
- Microservices architecture

## Contributing

We welcome contributions to improve the workshop:

1. **Bug Reports**: Open issues for any problems found
2. **Enhancements**: Suggest improvements or new examples
3. **Documentation**: Help improve explanations and guides
4. **Examples**: Share your own agent implementations

## License

This workshop is provided under the MIT License. See LICENSE file for details.

## Acknowledgments

Built with the [Strands Agents](https://strandsagents.com) framework. Special thanks to the Strands community for feedback and contributions.

---

**Ready to build intelligent agents? Start with notebook 01 and begin your journey!**
