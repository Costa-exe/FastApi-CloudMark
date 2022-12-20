from fastapi import FastAPI
from routes import companyClientRoutes, companyRoutes, clientRoutes, assignmentRoutes, assignmentEmployeeRoutes, contractTypeRoutes, employeeCompanyRoutes, employeeRoutes

app = FastAPI()

app.include_router(companyRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(companyClientRoutes.router)
app.include_router(assignmentRoutes.router)
app.include_router(assignmentEmployeeRoutes.router)
app.include_router(contractTypeRoutes.router)
app.include_router(employeeRoutes.router)
app.include_router(employeeCompanyRoutes.router)
