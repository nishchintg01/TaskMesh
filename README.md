# TaskMesh
Distributed Workflow Orchestration platform that enables users to create, schedule, and execute automated workflows consisting of interconnected tasks

User
 │
 └──────────────┐
                │
             Project
                │
                │
          Workflow
          ├─────────┐
          │         │
        Node      Edge
          │
          │
      TaskExecution
                │
         WorkflowExecution


Project Structure

taskmesh/
│
├── app/
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── health.py
│   │       │   ├── auth.py
│   │       │   ├── users.py
│   │       │   ├── projects.py
│   │       │   ├── workflows.py
│   │       │   └── executions.py
│   │       │
│   │       └── router.py
│   │
│   ├── auth/
│   │   ├── jwt.py
│   │   ├── dependencies.py
│   │   └── permissions.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   ├── constants.py
│   │   └── exceptions.py
│   │
│   ├── database/
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── middleware/
│   │   ├── request_id.py
│   │   ├── logging.py
│   │   └── timing.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── workflow.py
│   │   ├── node.py
│   │   └── execution.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── project_repository.py
│   │   └── workflow_repository.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── workflow.py
│   │   └── execution.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   ├── workflow_service.py
│   │   └── execution_service.py
│   │
│   ├── tasks/
│   │   └── README.md
│   │
│   ├── workers/
│   │   └── README.md
│   │
│   └── main.py
│
├── tests/
│   ├── api/
│   ├── services/
│   └── repositories/
│
├── migrations/
│
├── docker/
│
├── scripts/
│
├── docs/
│   ├── ADR/
│   ├── architecture/
│   └── engineering_journal/
│
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── README.md
└── uv.lock