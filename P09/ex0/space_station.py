#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_station.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 15:32:24 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/23 16:19:24 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Exercise 0: Space Station Data Validation.

Basic Pydantic model creation, field limits validation and exception handling.
"""

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    """Pydantic model representing the data of a Space Station"""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    """Valid and Invalid model creation, with error handling"""

    print("Space Station Data Validation")
    print("========================================")

    # Creating a valid space station instance
    station = SpaceStation(
        station_id="ISS001",
        name="Internation Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Non-Operational")

    print("")
    print("========================================")
    print("Expected validation error:")

    # Trying to create an invalid station instance (crew_size > 20)
    try:
        SpaceStation(
            station_id="ISS001",
            name="Internation Space Station",
            crew_size=200,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    # Catch validation error
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
