from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_to_transport_response_202_data import (
        StoreToTransportResponse202Data,
    )


T = TypeVar("T", bound="StoreToTransportResponse202")


@attr.s(auto_attribs=True)
class StoreToTransportResponse202:
    """
    Example:
        {'message': 'Upload process started. You can check the status of the process via api with the given id.',
            'data': {'id': '93be0c83-6ce5-456a-936b-81ee3b486149'}}

    Attributes:
        message (Union[Unset, str]):  Example: Upload process started. You can check the status of the process via api
            with the given id..
        data (Union[Unset, StoreToTransportResponse202Data]):  Example: {'id': '93be0c83-6ce5-456a-936b-81ee3b486149'}.
    """

    message: Union[Unset, str] = UNSET
    data: Union[Unset, "StoreToTransportResponse202Data"] = UNSET
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
        from ..models.store_to_transport_response_202_data import (
            StoreToTransportResponse202Data,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, StoreToTransportResponse202Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = StoreToTransportResponse202Data.from_dict(_data)

        store_to_transport_response_202 = cls(
            message=message,
            data=data,
        )

        store_to_transport_response_202.additional_properties = d
        return store_to_transport_response_202

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
