FROM python
ADD ./app /app
WORKDIR /app
RUN pip install -r requirements.txt