# Setup Instructions

Complete setup guide for the Strands Agents Workshop.

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Operating System**: macOS, Linux, or Windows
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 2GB free space

### AWS Requirements
- AWS Account with active subscription
- AWS CLI installed and configured
- Bedrock service access in your region
- IAM permissions for Bedrock model access

## Installation Steps

### 1. Environment Setup

```bash
# Clone or download the workshop
cd strands-agents-workshop

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Verify Python version
python --version  # Should be 3.8+
```

### 2. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
python -c "import strands_agents; print('Strands Agents installed successfully')"
```

### 3. AWS Configuration

#### Option A: AWS CLI Configuration
```bash
# Install AWS CLI if not already installed
pip install awscli

# Configure AWS credentials
aws configure
# Enter your:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region (e.g., us-west-2)
# - Default output format (json)
```

#### Option B: Environment Variables
```bash
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=us-west-2
```

#### Option C: AWS Profile
```bash
export AWS_PROFILE=your-profile-name
export AWS_REGION=us-west-2
```

### 4. Verify AWS Bedrock Access

```bash
# Test Bedrock access
aws bedrock list-foundation-models --region us-west-2

# Should return a list of available models
```

### 5. Optional: Ollama Setup (Local Models)

```bash
# Install Ollama (macOS/Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# For Windows, download from: https://ollama.ai/download

# Pull recommended models
ollama pull llama3.2:1b    # Lightweight model
ollama pull llama3.2:3b    # Balanced model

# Verify installation
ollama list
```

### 6. Optional: Memory Configuration

```bash
# Sign up for free Mem0 account at https://mem0.ai
# Get your API key from the dashboard

# Set environment variable
export MEM0_API_KEY=your-mem0-api-key

# Or create .env file
echo "MEM0_API_KEY=your-mem0-api-key" > .env
```

## Verification

### Test Your Setup

```bash
# Test Jupyter notebooks
jupyter notebook notebooks/01-basic-agent-creation.ipynb

# Test Python scripts
cd scripts
python 01_basic_agents.py
```

### Quick Health Check

```python
# Run this in Python to verify everything works
import strands_agents
import boto3
import jupyter

print("✅ All dependencies installed successfully!")
print(f"Strands Agents version: {strands_agents.__version__}")
print(f"AWS region: {boto3.Session().region_name}")
```

## Troubleshooting

### Common Issues

**1. Python Version Error**
```bash
# Check Python version
python --version
# If < 3.8, install newer Python version
```

**2. AWS Credentials Not Found**
```bash
# Check AWS configuration
aws sts get-caller-identity
# Should return your AWS account info
```

**3. Bedrock Access Denied**
- Ensure your AWS account has Bedrock access enabled
- Check IAM permissions for Bedrock service
- Verify you're using a supported region

**4. Import Errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**5. Jupyter Not Starting**
```bash
# Install Jupyter kernel
python -m ipykernel install --user --name=venv
jupyter notebook --generate-config
```

### Getting Help

1. Check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
2. Verify all prerequisites are met
3. Ensure virtual environment is activated
4. Check AWS credentials and permissions

## Next Steps

Once setup is complete:

1. **Start with Notebooks**: `jupyter notebook notebooks/`
2. **Or try Scripts**: `cd scripts && python 01_basic_agents.py`
3. **Follow the Learning Path** in the main README.md

---

**Setup complete! Ready to build intelligent agents! 🚀**
