FROM scoringengine/base

COPY bin/setup /app/bin/setup
COPY bin/competition.yaml /app/bin/competition.yaml

COPY scoring_engine /app/scoring_engine
USER root
RUN chmod -R 777 /app
RUN chmod -R 777 /home
USER engine
RUN pip install -e .

CMD ["./wait-for-port.sh", "mysql:3306", "python", "/app/bin/setup"]
