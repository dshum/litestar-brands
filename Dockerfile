# build stage
FROM python:3.12-slim-bookworm AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy project files
COPY pyproject.toml pdm.lock README.md /project/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.12-slim-bookworm

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.12/lib /project/pkgs

# retrieve executables
COPY --from=builder /project/__pypackages__/3.12/bin/* /bin/

# copy folders
COPY src/ /project/src
COPY resources/ /project/resources
COPY public/ /project/public

WORKDIR /project

# set command/entrypoint, adapt to fit your needs
CMD ["uvicorn", "src.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]