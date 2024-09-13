from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.read_input_file_next_batch_response_200_data_item import (
        ReadInputFileNextBatchResponse200DataItem,
    )


T = TypeVar("T", bound="ReadInputFileNextBatchResponse200")


@attr.s(auto_attribs=True)
class ReadInputFileNextBatchResponse200:
    """
    Example:
        {'message': '', 'data': [{'id': '1', 'name': 'first product'}]}

    Attributes:
        message (Union[Unset, None, str]):
        data (Union[Unset, List['ReadInputFileNextBatchResponse200DataItem']]):  Example: [{'id': '1', 'name': 'first
            product'}].
    """

    message: Union[Unset, None, str] = UNSET
    data: Union[Unset, List["ReadInputFileNextBatchResponse200DataItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

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
        from ..models.read_input_file_next_batch_response_200_data_item import (
            ReadInputFileNextBatchResponse200DataItem,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ReadInputFileNextBatchResponse200DataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        read_input_file_next_batch_response_200 = cls(
            message=message,
            data=data,
        )

        read_input_file_next_batch_response_200.additional_properties = d
        return read_input_file_next_batch_response_200

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
