# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Unsubscribe"]


class Unsubscribe(BaseModel):
    description: str
    """Details of the result of the unsubscribe action"""

    status: Literal["Unsubscribe successful", "Unsubscribe unsuccessful"]

    status_code: int = FieldInfo(alias="statusCode")
    """Status Code"""

    subscription_id: Optional[int] = FieldInfo(alias="subscriptionId", default=None)
    """ID for the Subscription"""

    subscription_provider_id: Optional[int] = FieldInfo(alias="subscriptionProviderId", default=None)
    """Identity of the subscription provider hosting the subscription"""
