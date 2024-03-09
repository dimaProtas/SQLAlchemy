from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from models import Workload


class WorkersAddDTO(BaseModel):
    username: str


class WorkersDTO(WorkersAddDTO):
    id: int


class ResumeAddDTO(BaseModel):
    title: str
    compensation: Optional[int]
    workload: Workload
    worker_id: int


class ResumeDTO(ResumeAddDTO):
    id: int
    created_at: datetime
    updated_at: datetime


class RsumeRelDTO(ResumeDTO):
    worker: "WorkersDTO"


class WorkerRelDTO(WorkersDTO):
    resume: list["ResumeDTO"]


class VacanciesAddDTO(BaseModel):
    title: str
    compensation: Optional[int]


class VacanciesDTO(VacanciesAddDTO):
    id: int


class VacanciesWithoutCompensationDATO(BaseModel):
    id: int
    title: str


class ResumeRelVacanciesRepliedDTO(BaseModel):
    worker: "WorkersDTO"
    vacancies_replied: list["VacanciesDTO"]


class ResumesRelVacanciesRepliedWithoutVacancyCompensationDTO(ResumeDTO):
    worker: "WorkersDTO"
    vacancies_replied: list["VacanciesWithoutCompensationDATO"]