from sqlalchemy import create_engine, text, inspect

class PostgreHandler:

    def __init__(self, url, tables):
        self.engine = create_engine(url)
        self.insp = inspect(self.engine)

        self.initialize_objects(tables)

    def run_query(self, query, data=[], is_select=False):
        with self.engine.connect() as conn:
            try:
                if is_select:
                    return conn.execute(text(query))
                else:
                    conn.execute(text(query), data)
                conn.commit()
            except Exception as err:
                conn.rollback()

    def initialize_objects(self, obj: dict):
        for table, create in obj.items():
            if self.insp.has_table(table):
                continue

            self.run_query(create)


if __name__ == '__main__':
    from initial_scripts import db_tables
    url = "postgresql://postgres:postgres@localhost:5432/postgres"
    test = PostgreHandler(url, db_tables)
