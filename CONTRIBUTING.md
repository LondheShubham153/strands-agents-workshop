# Contributing to Strands Agents Workshop

Thank you for your interest in improving the Strands Agents Workshop! This guide will help you contribute effectively.

## 🎯 Contribution Guidelines

### Types of Contributions

We welcome contributions in the following areas:

- **Bug fixes** in notebooks or scripts
- **Documentation improvements**
- **New examples** or use cases
- **Performance optimizations**
- **Setup and configuration enhancements**
- **Translation** of content

### What We Don't Accept

- Breaking changes to existing workshop flow
- Dependencies that significantly increase setup complexity
- Content that requires paid services beyond AWS
- Examples that compromise security best practices

## 🚀 Getting Started

### 1. Setup Development Environment

```bash
# Fork and clone the repository
git clone your-fork-url
cd strands-agents-workshop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install black isort pytest jupyter
```

### 2. Development Workflow

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Format code
black scripts/
isort scripts/

# Test your changes
pytest scripts/
jupyter nbconvert --execute notebooks/*.ipynb
```

## 📝 Content Standards

### Notebook Guidelines

- **Clear explanations** before each code block
- **Working examples** that run without modification
- **Progressive complexity** building on previous concepts
- **Error handling** demonstrations
- **Comments** explaining key concepts

### Script Guidelines

- **PEP 8** compliant code formatting
- **Type hints** where appropriate
- **Docstrings** for functions and classes
- **Error handling** with informative messages
- **Modular design** for reusability

### Documentation Standards

- **Clear headings** and structure
- **Code examples** with expected output
- **Prerequisites** clearly stated
- **Troubleshooting** sections where needed
- **Links** to relevant resources

## 🧪 Testing Requirements

### Before Submitting

1. **Test all notebooks** execute without errors
2. **Verify scripts** run in clean environment
3. **Check documentation** for accuracy
4. **Validate setup instructions** on fresh system
5. **Ensure AWS costs** remain minimal

### Testing Commands

```bash
# Test notebook execution
jupyter nbconvert --execute --to notebook notebooks/*.ipynb

# Test Python scripts
cd scripts
python -m pytest

# Test setup process
./test_setup.sh  # If available
```

## 📋 Submission Process

### 1. Prepare Your Contribution

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Examples work as expected
- [ ] No sensitive data included

### 2. Submit Pull Request

1. **Push** your feature branch
2. **Create** pull request with clear description
3. **Include** testing instructions
4. **Reference** any related issues
5. **Wait** for review and feedback

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Notebooks execute successfully
- [ ] Scripts run without errors
- [ ] Documentation is accurate
- [ ] Setup instructions verified

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added where needed
- [ ] Tests pass
```

## 🔧 Development Tips

### Working with Notebooks

```bash
# Clear notebook outputs before committing
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb

# Validate notebook structure
python scripts/verify_notebooks.py
```

### Code Quality

```bash
# Format Python code
black scripts/ --line-length 88
isort scripts/ --profile black

# Check code quality
flake8 scripts/
mypy scripts/
```

### Testing Locally

```bash
# Test individual components
python scripts/01_basic_agents.py
python scripts/02_agent_tools.py

# Test full workshop flow
./run_full_test.sh  # If available
```

## 📚 Resources

### Documentation
- [Strands Agents Documentation](https://docs.strands.ai)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Jupyter Best Practices](https://jupyter.org/community)

### Style Guides
- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Jupyter Notebook Best Practices](https://jupyter.org/community)

## 🆘 Getting Help

### Questions or Issues?

1. **Check existing issues** in the repository
2. **Review documentation** and setup guides
3. **Test in clean environment** to reproduce
4. **Create detailed issue** with reproduction steps

### Contact

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Email security issues privately

## 🎉 Recognition

Contributors will be:
- **Listed** in the contributors section
- **Credited** in release notes
- **Acknowledged** in workshop materials

Thank you for helping make this workshop better for everyone! 🚀
