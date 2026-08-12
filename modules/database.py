import sqlite3

class EvidenceDatabase:

    def __init__(self, database_path = "data/evidence.db"):
        self.database_path = database_path
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_table(self):
        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS evidence(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id TEXT UNIQUE NOT NULL,
                user_id TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                message TEXT NOT NULL,
                prediction TEXT NOT NULL,
                hash_value TEXT NOT NULL
            )

        """)

        connection.commit()
        connection.close()

    def insert_evidence(self, evidence, hash_value):

        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO evidence (
                message_id,
                user_id,
                timestamp,
                message,
                prediction,
                hash_value
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            evidence["message_id"],
            evidence["user_id"],
            evidence["timestamp"],
            evidence["message"],
            evidence["prediction"],
            hash_value
        ))

        connection.commit()
        connection.close()

    def get_all_evidence(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                message_id,
                user_id,
                timestamp,
                message,
                prediction,
                hash_value
            FROM evidence
        """)

        records = cursor.fetchall()

        connection.close()

        return records

    def get_evidence_by_id(self, message_id):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                message_id,
                user_id,
                timestamp,
                message,
                prediction,
                hash_value
            FROM evidence
            WHERE message_id = ?
        """, (message_id,))

        record = cursor.fetchone()

        connection.close()

        return record