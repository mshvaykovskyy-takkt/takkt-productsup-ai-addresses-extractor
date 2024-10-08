from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.items_count_input_file_response_200_data import (
        ItemsCountInputFileResponse200Data,
    )


T = TypeVar("T", bound="ItemsCountInputFileResponse200")


@attr.s(auto_attribs=True)
class ItemsCountInputFileResponse200:
    """
    Example:
        {'message': 'Items counted successfully.', 'data': {'count': 3}}

    Attributes:
        message (Union[Unset, str]):  Example: Items counted successfully..
        data (Union[Unset, ItemsCountInputFileResponse200Data]):  Example: {'count': 3}.
    """

    message: Union[Unset, str] = UNSET
    data: Union[Unset, "ItemsCountInputFileResponse200Data"] = UNSET
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
        from ..models.items_count_input_file_response_200_data import (
            ItemsCountInputFileResponse200Data,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ItemsCountInputFileResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ItemsCountInputFileResponse200Data.from_dict(_data)

        items_count_input_file_response_200 = cls(
            message=message,
            data=data,
        )

        items_count_input_file_response_200.additional_properties = d
        return items_count_input_file_response_200

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
