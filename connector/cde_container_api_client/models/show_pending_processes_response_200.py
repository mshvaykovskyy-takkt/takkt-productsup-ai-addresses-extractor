from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.show_pending_processes_response_200_data_item import (
        ShowPendingProcessesResponse200DataItem,
    )


T = TypeVar("T", bound="ShowPendingProcessesResponse200")


@attr.s(auto_attribs=True)
class ShowPendingProcessesResponse200:
    """
    Example:
        {'message': '', 'data': [{'id': 'b89dd936-13d0-48aa-baf6-f2728c4007de', 'status': 'running', 'exit-code': 1,
            'seconds-remaining': 21600}, {'id': '2716b6f0-db0c-4c59-a549-a56daad659ed', 'status': 'running', 'exit-code':
            None, 'seconds-remaining': 21600}]}

    Attributes:
        message (Union[Unset, None, str]):
        data (Union[Unset, List['ShowPendingProcessesResponse200DataItem']]):  Example: [{'id': 'b89dd936-13d0-48aa-
            baf6-f2728c4007de', 'status': 'running', 'exit-code': 1, 'seconds-remaining': 21600}, {'id':
            '2716b6f0-db0c-4c59-a549-a56daad659ed', 'status': 'running', 'exit-code': None, 'seconds-remaining': 21600}].
    """

    message: Union[Unset, None, str] = UNSET
    data: Union[Unset, List["ShowPendingProcessesResponse200DataItem"]] = UNSET
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
        from ..models.show_pending_processes_response_200_data_item import (
            ShowPendingProcessesResponse200DataItem,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ShowPendingProcessesResponse200DataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        show_pending_processes_response_200 = cls(
            message=message,
            data=data,
        )

        show_pending_processes_response_200.additional_properties = d
        return show_pending_processes_response_200

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
