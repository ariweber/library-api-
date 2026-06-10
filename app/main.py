from fastapi import FastAPI
from routers.book.routes import router as router_book
from routers.member.routes import router as router_member
from routers.report.routes import router as router_report

app = FastAPI()

app.include_router(router_book)
app.include_router(router_member)
app.include_router(router_report)



