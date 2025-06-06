# Playground for Testing and Learning Code

This is a multi-language playground repository for experimenting with different technologies,
frameworks, and language features.

## Mermaid Diagrams for VS Code Extension Testing

The following Mermaid diagrams are included to test VS Code GUI extensions and visualization
capabilities.

### Project Architecture Overview

```mermaid
graph TB
    A[Multi-Language Playground] --> B[Java Projects]
    A --> C[Python Scripts]
    A --> D[JavaScript/TypeScript]
    A --> E[C++ Examples]

    B --> B1[Maven Structure]
    B --> B2[Modern Java Features]
    B --> B3[JUnit Tests]

    C --> C1[Python 3.12+ Features]
    C --> C2[LeetCode Solutions]
    C --> C3[SQL Examples]

    D --> D1[TypeScript Examples]
    D --> D2[Modern JS Features]

    E --> E1[Core C++ Concepts]
```

### Development Workflow

```mermaid
flowchart LR
    A[Code Experiment] --> B{Choose Language}
    B -->|Java| C[Maven Build]
    B -->|Python| D[uv Environment]
    B -->|JS/TS| E[npm/bun Setup]
    B -->|C++| F[Compile & Run]

    C --> G[Run Tests]
    D --> H[pytest]
    E --> I[Jest Testing]
    F --> J[Execute Binary]

    G --> K[Deploy/Share]
    H --> K
    I --> K
    J --> K
```

### Class Diagram Example

```mermaid
classDiagram
    class App {
        +main(String[] args)
        +greetUser(String name)
    }

    class ModernJavaExample {
        +demonstrateRecords()
        +demonstrateStreams()
        +demonstrateOptional()
    }

    class LeetCodeSolutions {
        +twoSum(int[] nums, int target)
        +reverseString(char[] s)
        +isValidParentheses(String s)
    }

    App --> ModernJavaExample
    App --> LeetCodeSolutions
```

### Sequence Diagram - Testing Process

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant IDE as VS Code
    participant Test as Test Runner
    participant CI as CI/CD

    Dev->>IDE: Write Code
    IDE->>Dev: Syntax Highlighting
    Dev->>Test: Run Tests
    Test->>Dev: Test Results
    Dev->>CI: Push to Repository
    CI->>CI: Run All Tests
    CI->>Dev: Build Status
```

### Git Workflow

```mermaid
gitgraph
    commit id: "Initial setup"
    branch feature/java-examples
    checkout feature/java-examples
    commit id: "Add Maven structure"
    commit id: "Modern Java features"
    checkout main
    merge feature/java-examples
    branch feature/python-examples
    checkout feature/python-examples
    commit id: "Python 3.12 features"
    commit id: "LeetCode solutions"
    checkout main
    merge feature/python-examples
    commit id: "Update documentation"
```

### Technology Stack Timeline

```mermaid
timeline
    title Technology Learning Timeline

    2024 Q1 : Java 21 LTS
           : Maven Setup
           : JUnit 5

    2024 Q2 : Python 3.12
           : uv Package Manager
           : Type Hints

    2024 Q3 : TypeScript 5.0
           : Modern JS Features
           : Bun Runtime

    2024 Q4 : C++ Modernization
           : Performance Testing
           : Documentation
```

### State Diagram - Development Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Planning
    Planning --> Development
    Development --> Testing
    Testing --> Review
    Review --> Deploy
    Deploy --> Monitoring
    Monitoring --> Planning

    Testing --> Development : Bugs Found
    Review --> Development : Changes Requested
    Monitoring --> Development : Issues Detected

    Deploy --> [*] : Project Complete
```

### Entity Relationship Diagram

```mermaid
erDiagram
    PROJECT ||--o{ LANGUAGE : contains
    LANGUAGE ||--o{ EXAMPLE : has
    LANGUAGE ||--o{ TEST : includes
    EXAMPLE ||--o{ FEATURE : demonstrates

    PROJECT {
        string name
        string description
        date created
    }

    LANGUAGE {
        string name
        string version
        string package_manager
    }

    EXAMPLE {
        string filename
        string description
        string difficulty_level
    }

    TEST {
        string test_name
        string framework
        boolean passing
    }

    FEATURE {
        string name
        string category
        string documentation_link
    }
```

### User Journey Map

```mermaid
journey
    title Developer Learning Journey
    section Setup
      Install VS Code: 5: Developer
      Install Extensions: 4: Developer
      Clone Repository: 5: Developer
    section Java Learning
      Setup Maven: 3: Developer
      Write First App: 4: Developer
      Run Tests: 5: Developer
    section Python Learning
      Setup uv Environment: 4: Developer
      Try Modern Features: 5: Developer
      Solve LeetCode: 3: Developer
    section TypeScript Learning
      Configure TypeScript: 3: Developer
      Modern JS Features: 4: Developer
      Build Project: 5: Developer
```

## Project Structure

````markdown name=structure.md
```
playground/
├── src/main/java/          # Java source code
├── python/                 # Python experiments
├── ts/                     # TypeScript examples
├── cpp/                    # C++ code
├── docs/                   # Documentation
└── target/                 # Build artifacts
```
````
