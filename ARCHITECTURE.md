# Calculator CI Architecture

## Architecture Diagram

```mermaid
flowchart TD
    A["Developer<br/>Writes Calculator Code"]
    B["GitHub Repository<br/>Source Code + Unit Tests"]
    C["GitHub Actions<br/>Triggered on Push or Pull Request"]
    D["Build Docker Image"]
    E["Run 9 Unit Tests<br/>Inside Docker Container"]
    F["CI Successful"]
    G["CI Failed"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G

    style A fill:#DCEBFF,stroke:#3973AC,color:#111111
    style B fill:#DCEBFF,stroke:#3973AC,color:#111111
    style C fill:#E8DFFF,stroke:#805AD5,color:#111111
    style D fill:#DDF5E3,stroke:#39834A,color:#111111
    style E fill:#DDF5E3,stroke:#39834A,color:#111111
    style F fill:#C8F7D2,stroke:#25803D,color:#111111
    style G fill:#FFE0E0,stroke:#C53030,color:#111111
```

## Workflow Explanation

1. **Developer:** Writes or modifies the calculator code.
2. **GitHub Repository:** Stores the calculator, unit tests, and Docker configuration.
3. **GitHub Actions:** Automatically starts the CI workflow on configured pushes and pull requests.
4. **Build Docker Image:** Packages the application, Python runtime, and dependencies.
5. **Run Unit Tests:** Executes all 9 tests inside the Docker container.
6. **CI Result:** Reports success when the tests pass or failure when the build or tests fail.

## Scope

This diagram represents the implemented CI pipeline.