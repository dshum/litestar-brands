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

# copy app
COPY backend/ /project/src

# copy SSH key
COPY id_rsa /etc/ssh/key

RUN chmod 600 /etc/ssh/key \
    && chmod 755 /etc/ssh/ \
    && chown -R www-data:www-data /etc/ssh/key

WORKDIR /project

# set command/entrypoint, adapt to fit your needs
#CMD ["uvicorn", "src.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]