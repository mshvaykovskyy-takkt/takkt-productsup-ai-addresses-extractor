from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csa_classifications_list_response_200_data_item import (
        CsaClassificationsListResponse200DataItem,
    )


T = TypeVar("T", bound="CsaClassificationsListResponse200")


@attr.s(auto_attribs=True)
class CsaClassificationsListResponse200:
    """
    Example:
        {'message': 'successful operation', 'data': [{'classification-id': 111, 'classification-path': 'First
            category'}, {'classification-id': 222, 'classification-path': 'Second category'}]}

    Attributes:
        message (Union[Unset, str]):  Example: successful operation.
        data (Union[Unset, List['CsaClassificationsListResponse200DataItem']]):  Example: [{'classification-id': 111,
            'classification-path': 'First category'}, {'classification-id': 222, 'classification-path': 'Second category'}].
    """

    message: Union[Unset, str] = UNSET
    data: Union[Unset, List["CsaClassificationsListResponse200DataItem"]] = UNSET
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
        from ..models.csa_classifications_list_response_200_data_item import (
            CsaClassificationsListResponse200DataItem,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = CsaClassificationsListResponse200DataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        csa_classifications_list_response_200 = cls(
            message=message,
            data=data,
        )

        csa_classifications_list_response_200.additional_properties = d
        return csa_classifications_list_response_200

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
