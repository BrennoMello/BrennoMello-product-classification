# Use Python 3.9.1
FROM python:3.8.13-slim AS development

# Build arguments to set non-root user
ARG USER_ID=1000
ARG GROUP_ID=1000

# Environment variables to configure app
ENV API_HOST="0.0.0.0" \
    API_PORT="80" \
    API_GROUP="fastapi" \
    API_USER="fastapi" \
    API_DIR="/usr/src/api" \
    FASTAPI_HOME="/home/fastapi" \
    FASTAPI_ENV="development" \
    FASTAPI_APP="app.py"

# Work directory inside container
WORKDIR ${API_DIR}

# Install Debian Slim packages
ADD packages.txt .
RUN apt-get update -y -qq && xargs -ra packages.txt apt-get install -y -qq

# Install Python packages
ADD requirements.txt .
RUN pip install -r requirements.txt

# Add all other files to the container
ADD . .

# Create non-root users with appropriate permissions
RUN groupadd -g ${GROUP_ID} ${API_GROUP} \
  && useradd -u ${USER_ID} -g ${API_GROUP} ${API_USER} \
  && mkdir ${FASTAPI_HOME}  \
  && chown ${USER_ID}:${GROUP_ID} ${API_DIR} ${FASTAPI_HOME} 
  

# Set non-root users 
USER ${USER_ID}:${GROUP_ID}

# Expose FastAPI to outside the container
EXPOSE ${API_PORT}

# By default, execute FastAPI
CMD ["uvicorn", "app:application", "--host",  "0.0.0.0",  "--port", "80"]