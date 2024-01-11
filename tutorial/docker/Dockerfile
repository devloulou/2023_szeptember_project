FROM postgres

ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_DB postgres

ENV test_env test

# ez egy elérési utvonal a containerben: /valami/my_folder/final/
COPY valami.txt /valami/my_folder/final/
COPY test.sql /docker-entrypoint-initdb.d/