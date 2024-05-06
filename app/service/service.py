"""_summary_

    Returns:
        _type_: _description_
"""
import json

from dateutil import parser


class Service:
    """_summary_"""

    def __init__(self, repository) -> None:
        self._repository = repository

    def insert_all_rooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        with open("input/rooms.json", encoding="utf-8") as file:
            items = [(i["id"], i["name"]) for i in json.load(file)]
            return self._repository.insert_rooms(items)

    def insert_all_students(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        with open("input/students.json", encoding="utf-8") as file:
            items = [
                (
                    i["id"],
                    str(parser.parse(i["birthday"])),
                    i["name"].split()[0],
                    i["name"].split()[1],
                    i["room"],
                    i["sex"],
                )
                for i in json.load(file)
            ]
            return self._repository.insert_students(items)

    def get_rooms_students_count(self):
        """_summary_"""
        items = self._repository.get_rooms_students_count()
        list_to_json = [{"room": i[0], "amount": i[1]} for i in items]
        with open("results/rooms_amount.json", "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)

    def get_rooms_with_different_sexes(self):
        """_summary_"""
        items = self._repository.get_rooms_with_different_sexes()
        list_to_json = [{"room": i[0]} for i in items]
        with open("results/rooms_with_different_sexes.json", "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)

    def get_five_rooms_with_least_age_average(self):
        """_summary_"""
        items = self._repository.get_five_rooms_with_least_age_average()
        list_to_json = [{"room": i[0]} for i in items]
        with open("results/five_rooms_lower_age_average.json", "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)

    def get_five_rooms_with_largest_age_differnce(self):
        """_summary_"""
        items = self._repository.get_five_rooms_with_largest_age_differnce()
        list_to_json = [{"room": i[0]} for i in items]
        with open("results/five_rooms_with_largest_age_differnce.json", "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)
