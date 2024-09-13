from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_log_input_context import WriteLogInputContext


T = TypeVar("T", bound="WriteLogInput")


@attr.s(auto_attribs=True)
class WriteLogInput:
    """
    Example:
        {'message': 'Success message', 'context': {'code': 10}}

    Attributes:
        message (Union[Unset, str]):  Example: Success message.
        context (Union[Unset, WriteLogInputContext]):  Example: {'code': 10}.
    """

    message: Union[Unset, str] = UNSET
    context: Union[Unset, "WriteLogInputContext"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.write_log_input_context import WriteLogInputContext

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _context = d.pop("context", UNSET)
        context: Union[Unset, WriteLogInputContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = WriteLogInputContext.from_dict(_context)

        write_log_input = cls(
            message=message,
            context=context,
        )

        write_log_input.additional_properties = d
        return write_log_input

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
