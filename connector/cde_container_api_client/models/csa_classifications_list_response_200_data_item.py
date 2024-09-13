from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsaClassificationsListResponse200DataItem")


@attr.s(auto_attribs=True)
class CsaClassificationsListResponse200DataItem:
    """
    Example:
        {'classification-id': 111, 'classification-path': 'First category'}

    Attributes:
        classification_id (Union[Unset, int]):  Example: 111.
        classification_path (Union[Unset, str]):  Example: First category.
    """

    classification_id: Union[Unset, int] = UNSET
    classification_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classification_id = self.classification_id
        classification_path = self.classification_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification_id is not UNSET:
            field_dict["classification-id"] = classification_id
        if classification_path is not UNSET:
            field_dict["classification-path"] = classification_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classification_id = d.pop("classification-id", UNSET)

        classification_path = d.pop("classification-path", UNSET)

        csa_classifications_list_response_200_data_item = cls(
            classification_id=classification_id,
            classification_path=classification_path,
        )

        csa_classifications_list_response_200_data_item.additional_properties = d
        return csa_classifications_list_response_200_data_item

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
