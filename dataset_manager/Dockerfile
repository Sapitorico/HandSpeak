FROM python:3.10

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN /venv/bin/pip install -r requirements.txt

ENTRYPOINT ["/venv/bin/python", "-c", "print('¡Entorno creado correctamente!')"]