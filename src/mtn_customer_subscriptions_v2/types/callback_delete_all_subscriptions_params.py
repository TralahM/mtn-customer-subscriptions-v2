# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallbackDeleteAllSubscriptionsParams"]


class CallbackDeleteAllSubscriptionsParams(TypedDict, total=False):
    description: Required[str]
    """Details of the result of the unsubscribe action"""

    status: Required[Literal["Unsubscribe successful", "Unsubscribe unsuccessful"]]

    status_code: Required[Annotated[int, PropertyInfo(alias="statusCode")]]
    """Status Code"""

    subscription_id: Annotated[int, PropertyInfo(alias="subscriptionId")]
    """ID for the Subscription"""

    subscription_provider_id: Annotated[int, PropertyInfo(alias="subscriptionProviderId")]
    """Identity of the subscription provider hosting the subscription"""
