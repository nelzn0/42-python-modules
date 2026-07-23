#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_crew.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 17:03:46 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/23 17:43:08 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Exercise 2: Space Crew Management.

Nested Pydantic models, field limits validation,
cross model validation.
"""

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    """List of fixed string options (enums)"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    @model_validator(mode='after')
    def validate_crew(self) -> 'CrewMember':
        """Optional crew validator"""
        if self.years_experience >= self.age:
            raise ValueError("Years of experience cannot exceed age")
        return self


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        """Validate the entire model after all fields have been validated"""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_cap_or_command = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )

        if not has_cap_or_command:
            raise ValueError(
                "Mission crew must include at least one Captain or Commander")

        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is not active.")

        return self


def main() -> None:
    """Valid and Invalid mission creation, with error handling"""

    print("Space Mission Crew Validation")
    print("========================================")

    # Creating crew members
    member1 = CrewMember(
        member_id="CM1",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=25,
        specialization="Mission Command",
        years_experience=5,
    )

    member2 = CrewMember(
        member_id="CM2",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=13,
    )

    member3 = CrewMember(
        member_id="CM3",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=40,
        specialization="Engineering",
        years_experience=20,
    )

    # Creating a space mission instance
    mission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[member1, member2, member3],
        launch_date=datetime.now()
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days}")
    print(f"Budget: {mission.budget_millions}")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name}  "
              f"({member.rank.value}) - {member.specialization}")
    print("========================================")
    print("Expected validation error:")

    # Trying to create an invalid mission instance
    # (No Commander or Captain)
    try:
        crew1 = CrewMember(
            member_id="CM1",
            name="Sarah Connor",
            rank=Rank.CADET,
            age=25,
            specialization="Mission Command",
            years_experience=5,
        )

        crew2 = CrewMember(
            member_id="CM2",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=13,
        )

        crew3 = CrewMember(
            member_id="CM3",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=40,
            specialization="Engineering",
            years_experience=20,
        )

        SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[crew1, crew2, crew3],
            launch_date=datetime.now()
        )

        # Catch validation error
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
