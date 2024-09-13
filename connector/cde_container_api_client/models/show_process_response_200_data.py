from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShowProcessResponse200Data")


@attr.s(auto_attribs=True)
class ShowProcessResponse200Data:
    """
    Example:
        {'id': '93e37cdf-046d-45b2-a983-1e2580e57b5c', 'status': 'running', 'exit-code': 12, 'seconds-remaining': 21600}

    Attributes:
        id (Union[Unset, str]):  Example: 93e37cdf-046d-45b2-a983-1e2580e57b5c.
        status (Union[Unset, str]):  Example: running.
        exit_code (Union[Unset, int]):  Example: 12.
        seconds_remaining (Union[Unset, int]):  Example: 21600.
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    exit_code: Union[Unset, int] = UNSET
    seconds_remaining: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status
        exit_code = self.exit_code
        seconds_remaining = self.seconds_remaining

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if exit_code is not UNSET:
            field_dict["exit-code"] = exit_code
        if seconds_remaining is not UNSET:
            field_dict["seconds-remaining"] = seconds_remaining

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        exit_code = d.pop("exit-code", UNSET)

        seconds_remaining = d.pop("seconds-remaining", UNSET)

        show_process_response_200_data = cls(
            id=id,
            status=status,
            exit_code=exit_code,
            seconds_remaining=seconds_remaining,
        )

        show_process_response_200_data.additional_properties = d
        return show_process_response_200_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
