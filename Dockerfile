FROM tiangolo/uwsgi-nginx-flask:python3.8
#FROM tiangolo/meinheld-gunicorn-flask:python3.9

ENV FLASK_ENV=development
ENV FLASK_APP=main.py

COPY ./app /app
COPY "entrypoint.sh" "/entrypoint.sh"
RUN chmod 755 /entrypoint.sh
COPY "envconsul" "/bin/envconsul"

RUN pip install -r /app/requirements.txt
#ENTRYPOINT ["/entrypoint.sh"]
#CMD ["/bin/envconsul", "-consul-addr","consul-ui.default.svc.cluster.local","--prefix=sample-app","/start.sh"]
#CMD ["/start.sh"]
