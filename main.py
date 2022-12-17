from fastapi import FastAPI
from routes import contract_typeRoutes, employeeRoutes, employee_companyRoutes

app = FastAPI()

app.include_router(contract_typeRoutes.router)
app.include_router(employeeRoutes.router)
app.include_router(employee_companyRoutes.router)
