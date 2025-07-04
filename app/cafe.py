from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise NotVaccinatedError
        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(0)
        else:
            return f"Welcome to {self.name}"
