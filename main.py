from fastapi import FastAPI
from routes import companyClientRoutes, companyRoutes, clientRoutes, assignmentRoutes, assignmentEmployeeRoutes, contractTypeRoutes, employeeCompanyRoutes, employeeRoutes
from fastapi.middleware.cors import CORSMiddleware

# origins = [
#     "*"
# ]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origin_regex='http://.*:4200/*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companyRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(companyClientRoutes.router)
app.include_router(assignmentRoutes.router)
app.include_router(assignmentEmployeeRoutes.router)
app.include_router(contractTypeRoutes.router)
app.include_router(employeeRoutes.router)
app.include_router(employeeCompanyRoutes.router)
