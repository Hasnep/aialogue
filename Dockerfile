FROM node:18 AS builder-node

WORKDIR /frontend

# Install Node dependencies
COPY frontend/package.json .
COPY frontend/package-lock.json .
RUN npm ci

# Build
COPY frontend .
RUN npm run build

FROM python:3.11 AS builder-python

WORKDIR /backend

# Install Poetry
RUN python3 -m pip install poetry==1.4.0

# Install Python dependencies in a venv
RUN python3 -m venv /venv
COPY backend/pyproject.toml .
COPY backend/poetry.lock .
RUN poetry export --format=requirements.txt --output=requirements.txt
RUN /venv/bin/python -m pip install -r requirements.txt

FROM python:3.11 AS runner

COPY --from=builder-python /venv /venv
COPY --from=builder-node /frontend/public /frontend/public

# Copy backend source code
COPY backend/aialogue /backend/aialogue

WORKDIR /backend

EXPOSE 8080
ENV PORT 8080

CMD ["/venv/bin/python","-m", "aialogue", "--static-folder", "/frontend/public"]
