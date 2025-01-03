# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-bookworm

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --no-deps -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "update_comps.py"]
