## Data Engineering

This repo is responsible for the storage solutions and processes that handle both vendor-supplied data and internally generated data.


**Repository Access:**

To fork the repository and start contributing, run the following command:

```bash
git clone https://github.com/Hawk-Center/data-engineering.git
```

## Documentation Standards

Comprehensive documentation is essential to ensure that future team members can efficiently debug and refactor our codebase. Clear and well-maintained documentation facilitates understanding, promotes consistency, and enhances overall project maintainability.

Example:

```python
"""
@description: Summary of what the file is
@author: [FIRST NAME] [LAST NAME]
    
"""

def sample_function(var: str) -> str:
    
    """Description of what the function is

    Args:
        var (str): description of what the 

    Returns:
        str: _description_
    """
    
    print
    
    # Inline comments to summarize more complex code
```

**Notes:**

1. Type-Annotate Code: Add type annotations to function signatures and variables to make the code more self-explanatory and to help catch potential issues early. For example, def greet(name: str) -> str:.
2. PEP8-Compliant 80-Char Max per Line: Follow the PEP8 style guide and keep lines to a maximum of 80 characters. This improves readability and ensures consistency across the codebase.

If you are using an LLM to write code for you, adding these instructions will usually get you code compliant with the above:
```
use type-annotations, google-style docstrings, and pep8 compliant max 80 chars per line.
```
