from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_to_output_file_response_400_errors import (
        WriteToOutputFileResponse400Errors,
    )


T = TypeVar("T", bound="WriteToOutputFileResponse400")


@attr.s(auto_attribs=True)
class WriteToOutputFileResponse400:
    """
    Example:
        {'message': 'Validation failed', 'errors': {'data': 'This value should be an array of items.'}}

    Attributes:
        message (Union[Unset, str]):  Example: Validation failed.
        errors (Union[Unset, WriteToOutputFileResponse400Errors]):  Example: {'data': 'This value should be an array of
            items.'}.
    """

    message: Union[Unset, str] = UNSET
    errors: Union[Unset, "WriteToOutputFileResponse400Errors"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.write_to_output_file_response_400_errors import (
            WriteToOutputFileResponse400Errors,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, WriteToOutputFileResponse400Errors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = WriteToOutputFileResponse400Errors.from_dict(_errors)

        write_to_output_file_response_400 = cls(
            message=message,
            errors=errors,
        )

        write_to_output_file_response_400.additional_properties = d
        return write_to_output_file_response_400

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
