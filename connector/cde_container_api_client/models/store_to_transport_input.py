from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreToTransportInput")


@attr.s(auto_attribs=True)
class StoreToTransportInput:
    """
    Example:
        {'source_file': '/example-subdirectory/example_file.txt', 'remote_file': '/remote-folder/remote_file.txt'}

    Attributes:
        source_file (Union[Unset, str]):  Example: /example-subdirectory/example_file.txt.
        remote_file (Union[Unset, str]):  Example: /remote-folder/remote_file.txt.
    """

    source_file: Union[Unset, str] = UNSET
    remote_file: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_file = self.source_file
        remote_file = self.remote_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_file is not UNSET:
            field_dict["source_file"] = source_file
        if remote_file is not UNSET:
            field_dict["remote_file"] = remote_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_file = d.pop("source_file", UNSET)

        remote_file = d.pop("remote_file", UNSET)

        store_to_transport_input = cls(
            source_file=source_file,
            remote_file=remote_file,
        )

        store_to_transport_input.additional_properties = d
        return store_to_transport_input

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
