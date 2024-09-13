from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_log_response_400_errors import WriteLogResponse400Errors


T = TypeVar("T", bound="WriteLogResponse400")


@attr.s(auto_attribs=True)
class WriteLogResponse400:
    """
    Example:
        {'message': 'Validation failed', 'errors': {'message': 'This value should not be blank.'}}

    Attributes:
        message (Union[Unset, str]):  Example: Validation failed.
        errors (Union[Unset, WriteLogResponse400Errors]):  Example: {'message': 'This value should not be blank.'}.
    """

    message: Union[Unset, str] = UNSET
    errors: Union[Unset, "WriteLogResponse400Errors"] = UNSET
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
        from ..models.write_log_response_400_errors import WriteLogResponse400Errors

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, WriteLogResponse400Errors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = WriteLogResponse400Errors.from_dict(_errors)

        write_log_response_400 = cls(
            message=message,
            errors=errors,
        )

        write_log_response_400.additional_properties = d
        return write_log_response_400

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
