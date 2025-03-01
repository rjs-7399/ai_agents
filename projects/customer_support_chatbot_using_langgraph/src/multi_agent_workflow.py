from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages
from pydantic import BaseModel, Field


def updated_dialog_stack(left: list[str], right: Optional[str]) -> list[str]:
    if right is None:
        return left
    if right == "pop":
        return left[:-1]
    return left + [right]


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str
    dialog_state: Annotated[
        list[
            Literal[
                "assistant",
                "update_flight",
                "book_car_rental",
                "book_hotel",
                "book_excursion",
            ]
        ],
        updated_dialog_stack,
    ]


class CompleteOrEscalate(BaseModel):
    """
        A tool to mark the current task as completed and/or to escalate control of the dialog to the main assistant,
        who can re-route the dialog based on the user's needs.
    """
    cancel: bool = True
    reason: str

    class Config:
        json_schema_extra = {
            "example": {
                "cancel": True,
                "reason": "User changed their mind about the current Task",
            },
            "example 2": {
                "cancel": True,
                "reason": "I have fully complete the task.",
            },
            "example 3": {
                "cancel": False,
                "reason": "I need to seach the user's email or calendar for more information",
            }
        }

