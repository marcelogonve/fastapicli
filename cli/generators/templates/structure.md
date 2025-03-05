folders:
    - app
    - app/api/v1/endpoints
    - app/core
    - app/models
    - app/schemas
    - app/services
    - app/db/migrations
    - app/tests
    - app/utils
    - docker    #Only Docker is activated

files:
    .gitignore: templates/.gitignore
    README.md: templates/README.md
    app/__init__.py: ""
    app/main.py: templates/main.py
    app/api/__init__.py: ""
    app/api/v1/__init__.py: ""
    app/api/v1/endpoints/__init__.py: ""
    app/core/__init__.py: ""
    app/core/config.py: templates/config.py
    app/core/security.py: templates/security.py
    app/models/__init__.py: ""
    app/schemas/__init__.py: ""
    app/services/__init__.py: ""
    app/db/__init__.py: ""
    app/db/base.py: templates/base.py
    app/db/session.py: templates/session.py
    app/tests/__init__.py: ""
    app/utils/__init__.py: ""
    app/utils/helpers.py: templates/helpers.py
    docker/Dockerfile: templates/Dockerfile #Only Docker is activated
    docker/docker-compose.yml: templates/docker-compose.yml #Only Docker is activated
    .env: templates/.env
    requirements.txt: templates/requirements.txt
    pyproject.toml: templates/pyproject.toml
