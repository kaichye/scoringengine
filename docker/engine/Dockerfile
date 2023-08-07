FROM scoringengine/base

COPY bin/engine /app/bin/engine

COPY scoring_engine /app/scoring_engine
USER root
RUN chmod -R 777 /app
RUN chmod -R 777 /home
USER engine
RUN pip install -e .

CMD ["./wait-for-container.sh", "bootstrap", "/app/bin/engine"]
