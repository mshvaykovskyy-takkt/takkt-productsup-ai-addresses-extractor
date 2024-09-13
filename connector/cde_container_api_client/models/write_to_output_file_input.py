from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_to_output_file_input_data_item import (
        WriteToOutputFileInputDataItem,
    )
    from ..models.write_to_output_file_input_meta import WriteToOutputFileInputMeta


T = TypeVar("T", bound="WriteToOutputFileInput")


@attr.s(auto_attribs=True)
class WriteToOutputFileInput:
    """
    Example:
        {'meta': {'separator': '-'}, 'data': [{'id': 1, 'taxon-0-id': 11, 'taxon-0-name': 'taxon0'}]}

    Attributes:
        meta (Union[Unset, WriteToOutputFileInputMeta]):  Example: {'separator': '-'}.
        data (Union[Unset, List['WriteToOutputFileInputDataItem']]):  Example: [{'id': 1, 'taxon-0-id': 11,
            'taxon-0-name': 'taxon0'}].
    """

    meta: Union[Unset, "WriteToOutputFileInputMeta"] = UNSET
    data: Union[Unset, List["WriteToOutputFileInputDataItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.write_to_output_file_input_data_item import (
            WriteToOutputFileInputDataItem,
        )
        from ..models.write_to_output_file_input_meta import WriteToOutputFileInputMeta

        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, WriteToOutputFileInputMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = WriteToOutputFileInputMeta.from_dict(_meta)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = WriteToOutputFileInputDataItem.from_dict(data_item_data)

            data.append(data_item)

        write_to_output_file_input = cls(
            meta=meta,
            data=data,
        )

        write_to_output_file_input.additional_properties = d
        return write_to_output_file_input

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
