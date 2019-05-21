FROM python

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000

STOPSIGNAL SIGINT

ENTRYPOINT [ "python", "manage.py" ]

CMD ["runserver", "0.0.0.0:8000"]