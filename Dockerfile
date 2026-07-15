FROM python:3.12-slim

# Install uv using the official multi-stage image binaries
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency tracking files
COPY pyproject.toml uv.lock ./

# Install dependencies strictly from lockfile into the container's .venv
RUN uv sync --frozen --no-cache --no-editable

# Place the virtual environment's executable path explicitly at the front of $PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application source code
COPY . .

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
