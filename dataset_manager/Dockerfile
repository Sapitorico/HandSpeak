FROM python:3.10

RUN python3 -m venv ./venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/echo", "Hello, $name"]