from fastapi import FastAPI
from routers.book.routes import router as router_book
from routers.member.routes import router as router_member
from routers.report.routes import router as router_report
from database.connection import get_connection, create_tables

app = FastAPI()

app.include_router(router_book)
app.include_router(router_member)
app.include_router(router_report)


if __name__ == "__main__":
    get_connection()
    a =create_tables()
    print(a)



