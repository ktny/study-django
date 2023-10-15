from logging import getLogger

import asyncpg

# from pg import connect
# from pgdb import connect

logger = getLogger(__name__)

dsn = "postgresql://postgres:pgpassword@db:5432/postgres"

# con = connect(dbname="postgres", host="db", port=5432, user="postgres", passwd="pgpassword", nowait=True)
# con = connect(dbname="postgres", host="db", port=5432, user="postgres", password="pgpassword")
# cursor = con.cursor()


async def get_data_from_asyncpg():
    logger.info("start get_data_from_asyncpg")

    async with asyncpg.create_pool(dsn) as pool:
        row = await pool.fetchrow(
            "select SUM(LENGTH(question_text)), AVG(LENGTH(question_text)), MIN(LENGTH(question_text)), MAX(LENGTH(question_text)) from polls_question;"
        )
        logger.info(row)
        return row

    # cursor.execute("select * from polls_question limit 10")
    # cursor.execute("select count(*) from polls_question")

    # cursor.execute(
    #     "select SUM(LENGTH(question_text)), AVG(LENGTH(question_text)), MIN(LENGTH(question_text)), MAX(LENGTH(question_text))  from polls_question"
    # )

    # query = con.query(
    #     "select SUM(LENGTH(question_text)), AVG(LENGTH(question_text)), MIN(LENGTH(question_text)), MAX(LENGTH(question_text))  from polls_question"
    # )

    # query = con.send_query(
    #     "select SUM(LENGTH(question_text)), AVG(LENGTH(question_text)), MIN(LENGTH(question_text)), MAX(LENGTH(question_text)) from polls_question;"
    # )

    # query = con.send_query("select SUM(LENGTH(question_text)) from polls_question;")
    # query = con.send_query("select pg_sleep(1)")
    # logger.info("start getresult")

    # questions = query.getresult()
    # query.getresult()

    # logger.info(questions)

    # logger.info("start fetchall")
    # questions = cursor.fetchall()

    # threads = threading.enumerate()
    # logger.info(f"全てのスレッド: {threads}")

    # count = questions[0][0]
    # logger.info(count)
    # return count
