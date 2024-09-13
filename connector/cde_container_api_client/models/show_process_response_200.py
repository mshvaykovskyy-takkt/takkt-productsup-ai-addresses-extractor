from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.show_process_response_200_data import ShowProcessResponse200Data


T = TypeVar("T", bound="ShowProcessResponse200")


@attr.s(auto_attribs=True)
class ShowProcessResponse200:
    """
    Example:
        {'message': '', 'data': {'id': '93e37cdf-046d-45b2-a983-1e2580e57b5c', 'status': 'running', 'exit-code': 12,
            'seconds-remaining': 21600}}

    Attributes:
        message (Union[Unset, None, str]):
        data (Union[Unset, ShowProcessResponse200Data]):  Example: {'id': '93e37cdf-046d-45b2-a983-1e2580e57b5c',
            'status': 'running', 'exit-code': 12, 'seconds-remaining': 21600}.
    """

    message: Union[Unset, None, str] = UNSET
    data: Union[Unset, "ShowProcessResponse200Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.show_process_response_200_data import ShowProcessResponse200Data

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ShowProcessResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ShowProcessResponse200Data.from_dict(_data)

        show_process_response_200 = cls(
            message=message,
            data=data,
        )

        show_process_response_200.additional_properties = d
        return show_process_response_200

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
